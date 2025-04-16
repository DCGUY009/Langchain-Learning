# 🔍 Understanding Tool Calling in LLMs and the Role of MCP

### 🧠 How LLMs Work  
LLMs (Large Language Models) are statistical models that predict the next token in a sequence based on prior context. They operate on a token-by-token basis using probability distributions.

![LLMs Behaviour](./Images/LLMs_Behaviour.png)

In tool-augmented agents, LLMs function as reasoning engines. For example, if you ask:  
**"What’s the weather in Hyderabad?"**,  
the LLM won’t hallucinate an answer if it lacks real-time info. Instead, it will generate a tool call like:  
```python
get_weather(city="Hyderabad")
```
This function call is executed externally (by the software engineer or application), and the result is returned to the LLM to continue generating the response.

---

### 🛠️ Tool Calling in LangChain vs MCP

Both **LangChain** and **Model Context Protocol (MCP)** allow tools to be defined and used by LLMs. A **tool** here is just a function that the LLM can invoke when needed.

#### Key Concepts:
- **Tools** are functions with:
  - A name
  - Arguments
  - Descriptions (important for model understanding)
  - A return value

![Tool Definition: Langchain vs MCP](./Images/Toolcalling_mcplangchain.png)

---

### 🔄 LangChain: Binding Tools Directly to the Model

In LangChain, you bind tools directly to the LLM using `bind_tools`, so the LLM itself chooses which tools to call and when.

```python
langchain_chat_model.bind_tools([my_tool])
```

![LangChain Tool Binding](./Images/langchain_mcp_difference.png)

---

### 🌐 MCP: Exposing Tools to Applications, Not Just LLMs

In MCP, tools aren’t injected directly into the LLM. Instead, they are **exposed by the MCP Server** and used by **AI applications** (like Cursor, Claude Desktop, Windsurf, LangGraph Agent, etc.) that wrap around the LLM.

So the **MCP Client** is responsible for:
- Injecting the right tools, prompts, and resources into the model context  
- Acting as an interface layer between model and the tools

![MCP Working](./Images/MCP_Working.png)

---

### 🔄 Summary of Differences

| Feature            | LangChain                               | MCP                                                   |
|--------------------|------------------------------------------|--------------------------------------------------------|
| Tool Binding       | Bound directly to LLM using `bind_tools` | Bound to AI application via MCP Server → MCP Client    |
| Tool Call Location | Model chooses tool                      | Application injects tool calls based on context        |
| Extensibility      | Tools only                               | Tools + Prompts + Resources                            |
| Clients            | LLMs (via LangChain)                     | AI apps like Cursor, Claude Desktop, LangGraph, etc.   |

---

### 🧩 Bonus: LangChain-MCP Adapter

There's also an open-source **LangChain-MCP adapter** that allows you to convert MCP tools into LangChain or LangGraph compatible tools. This means:
- You can re-use someone else's MCP Server tools in your LangChain application  
- No need for manual adaptation  
- Comes with an MCP client that supports connection to multiple MCP Servers