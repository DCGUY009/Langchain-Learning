# 🧠 Understanding Coreference Resolution in LLMs

## 📌 LLMs Are Stateless  

LLMs (Large Language Models) are **stateless**, meaning they **do not remember** past interactions in a conversation unless explicitly provided with context.

### ❌ Example: No Memory (Stateless)
```
User: Who created LangChain?
Bot: Harrison Chase

User: Does he have a YouTube channel?
Bot: I’m sorry, who are you referring to?
```
Here, the LLM fails to understand that **"he"** refers to *Harrison Chase* because it does not retain previous conversation context.

---

## 🔍 What is Coreference Resolution?

**Coreference Resolution** is the process of identifying words or phrases in a text that refer to the same entity. In our example, the word **"he"** refers to *Harrison Chase*, but since the LLM lacks memory, it cannot resolve the reference.

### ✅ Example: With Memory (Passing Chat History)
```
User: Who created LangChain?
Bot: Harrison Chase

User: 
Past Conversation:
User: Who created LangChain?
Bot: Harrison Chase

New question: Does he have a YouTube channel?

Bot: Yes, he does!
```
By **including the past conversation** in the prompt, the LLM can correctly resolve **"he"** as *Harrison Chase*.

---

## 🖼️ Visualizing Coreference Resolution

![Coreference Resolution](coreference_resolution.png)

> This diagram shows how different words refer to the same entity. Similarly, in LLMs, we must **explicitly pass conversation history** to help the model resolve references.

---

## 🛠️ So, how is memory handled?

All memory handling techniques **boil down to one fundamental concept**:

> **We simply find sophisticated ways to pass conversation history into the prompt.**  

LangChain provides **memory modules** to efficiently manage conversation history by determining **what information** to pass in.

### 📌 Example: Passing Context in a Prompt
```
Given the {past_conversation}, answer my question:

Past conversation:
User 1: Hi, I like to drink Cold Brew coffee. Where can I find this?
Bot 1: You can find Cold Brew coffee at Starbucks.

User 2: I don’t like Starbucks. Is there anywhere else?
Bot 2: Yes, you can also find Cold Brew coffee at CoffeeBean.

Question: Where else can I find that?
```
Here, **"that"** correctly refers to *Cold Brew coffee* because we passed the past conversation as context.

---

## 🚧 The Challenge: Token Limitations  

However, including **entire chat histories** can quickly **exceed the model’s token limit**, especially in long conversations (e.g., 1-hour chat sessions).

### 🛠️ Solution: LangChain’s Memory Strategies  
To handle this, LangChain provides **various memory management techniques** discussed in **[LangChain Memory Deep Dive.md](Langchain%20Memory%20Deep%20Dive.md)**.

---

## 🎯 Summary
- LLMs **don’t remember past chats** unless history is included in the prompt.
- **Coreference Resolution** helps identify references in a conversation.
- **LangChain manages memory** by selectively passing past conversations to the model.
- **Token limits** require optimized memory handling.
- **All memory solutions are just sophisticated ways of passing conversation history into the prompt.**  

---

This is the foundation of all **memory solutions in LangChain**—it’s all about **finding the best way to pass relevant context** to the model! 🚀

---
