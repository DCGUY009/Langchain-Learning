# LangChain Memory Deep Dive

Efficient memory handling is crucial in GeNAI applications to avoid context overflow and ensure relevant information is passed to the LLM. As the saying goes, *“Garbage in, garbage out.”* LangChain offers three primary strategies to manage memory effectively:

1. **Simple Message Stuffing**: Inject all previous messages directly into the prompt.
2. **Trimming Strategy**: Inject only recent messages by trimming older ones to reduce noise.
3. **Summary Strategy**: Synthesize summaries of past conversations to preserve key context efficiently.

---

## Where to Save Memory?

While we've discussed what and how to save memory, it's equally important to know **where** to store it. In LangGraph (used with LangChain), this is handled using **checkpoints**. These checkpoints make it easy to persist messages and manage memory across sessions.

Check out the [LangGraph course on Udemy](https://www.udemy.com/course/langgraph/?couponCode=KEEPLEARNING) to dive deeper.

In simple LangChain implementations, history is often stored in a local dictionary. However, in real-world applications, memory is persisted in a database and fetched as needed during runtime.

LangChain memory is typically managed using a `checkpointer`—an object responsible for storing and retrieving memory from persistent storage.

---

## 💬 LangChain Memory Techniques

### 1. Simple Message Stuffing (Pre-LangGraph)

```python
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content="You are a helpful assistant. Answer all questions to the best of your ability."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = prompt | model

ai_msg = chain.invoke(
    {
        "messages": [
            HumanMessage(content="Translate from English to French: I love programming."),
            AIMessage(content="J'adore la programmation."),
            HumanMessage(content="What did you just say?"),
        ],
    }
)
print(ai_msg.content)
```

---

### 2. LangGraph with Automatic History Management

```python
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

workflow = StateGraph(state_schema=MessagesState)

def call_model(state: MessagesState):
    system_prompt = "You are a helpful assistant. Answer all questions to the best of your ability."
    messages = [SystemMessage(content=system_prompt)] + state["messages"]
    response = model.invoke(messages)
    return {"messages": response}

workflow.add_node("model", call_model)
workflow.add_edge(START, "model")

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)
```

---

### 3. Trimming Messages

Trim older messages to reduce prompt size and keep recent context relevant.

```python
from langchain_core.messages import trim_messages
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

trimmer = trim_messages(strategy="last", max_tokens=2, token_counter=len)

workflow = StateGraph(state_schema=MessagesState)

def call_model(state: MessagesState):
    trimmed_messages = trimmer.invoke(state["messages"])
    system_prompt = "You are a helpful assistant. Answer all questions to the best of your ability."
    messages = [SystemMessage(content=system_prompt)] + trimmed_messages
    response = model.invoke(messages)
    return {"messages": response}

workflow.add_node("model", call_model)
workflow.add_edge(START, "model")

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)
```

---

### 4. Summary Memory for Long-Running Conversations

Summarize long histories to maintain coherence while minimizing prompt length.

```python
from langchain_core.messages import HumanMessage, RemoveMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

workflow = StateGraph(state_schema=MessagesState)

def call_model(state: MessagesState):
    system_prompt = (
        "You are a helpful assistant. "
        "Answer all questions to the best of your ability. "
        "The provided chat history includes a summary of the earlier conversation."
    )
    system_message = SystemMessage(content=system_prompt)
    message_history = state["messages"][:-1]

    if len(message_history) >= 4:
        last_human_message = state["messages"][-1]
        summary_prompt = (
            "Distill the above chat messages into a single summary message. "
            "Include as many specific details as you can."
        )
        summary_message = model.invoke(
            message_history + [HumanMessage(content=summary_prompt)]
        )

        delete_messages = [RemoveMessage(id=m.id) for m in state["messages"]]
        human_message = HumanMessage(content=last_human_message.content)
        response = model.invoke([system_message, summary_message, human_message])
        message_updates = [summary_message, human_message, response] + delete_messages
    else:
        message_updates = model.invoke([system_message] + state["messages"])

    return {"messages": message_updates}

workflow.add_node("model", call_model)
workflow.add_edge(START, "model")

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)
```

---

## 📌 Summary

- Use **message stuffing** for simple scenarios.
- Apply **message trimming** to control token usage.
- Employ **summary memory** for lengthy interactions.
- Leverage **LangGraph checkpoints** for persistent memory handling.

By using the right memory strategy, you can optimize your LLM apps for both cost-efficiency and coherence.

---
