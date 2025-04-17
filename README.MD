## This is me learning, unlearning and relearning Langchain from Eden Marco's Udemy Course

Course Link - [LangChain- Develop LLM powered applications with LangChain](https://www.udemy.com/course/langchain/?couponCode=KEEPLEARNING)

---

## Using This Project Effectively

### 📁 Folder Structure

```
.vscode/
Code Interpreter/
  └── main.py
Documentation Helper/
  └── main.py
Ice breaker/
  └── ice_breaker.py
Ice breaker project/
  └── app.py
intro-to-vector-dbs/
  └── main.py
Langchain Theory Notes/
LLM Applications in Production/
Model Context Protocol/
Prompt Engineering Theory/
react-langchain/
  └── main.py
vectorstore-in-memory/
  └── main.py
.gitignore
README.md
```

---

### 🔁 Recommended Learning Order (LangChain-Focused)

To learn LangChain step-by-step using this repository, follow this order:

```
1. Ice breaker  
2. Ice breaker project  
3. react-langchain  
4. intro-to-vector-dbs  
5. vectorstore-in-memory  
6. Documentation Helper  
7. Code Interpreter
```

---

### ▶️ How to Run Each Component

Each project has its own virtual environment setup. Use the terminal and `cd` into the appropriate folder before running the commands.

---

#### 1. **Ice breaker**
- Navigate:  
  ```bash
  cd "Ice breaker"
  ```
- Activate environment:  
  ```bash
  ./.venv/Scripts/activate
  ```
- Run:  
  ```bash
  python ice_breaker.py
  ```

---

#### 2. **Ice breaker project** (HTML/CSS + Flask app)
- Navigate:  
  ```bash
  cd "Ice breaker project"
  ```
- Activate environment:  
  ```bash
  ./.venv/Scripts/activate
  ```
- Run:  
  ```bash
  python app.py
  ```

---

#### 3. **react-langchain**
- Navigate:  
  ```bash
  cd "react-langchain"
  ```
- Activate environment:  
  ```bash
  ./.venv/Scripts/activate
  ```
- Run:  
  ```bash
  python main.py
  ```

---

#### 4. **intro-to-vector-dbs**
- Navigate:  
  ```bash
  cd "intro-to-vector-dbs"
  ```
- Activate environment:  
  ```bash
  ./.venv/Scripts/activate
  ```
- Run:  
  ```bash
  python main.py
  ```

---

#### 5. **vectorstore-in-memory**
- Navigate:  
  ```bash
  cd "vectorstore-in-memory"
  ```
- Activate environment:  
  ```bash
  ./.venv/Scripts/activate
  ```
- Run:  
  ```bash
  python main.py
  ```

---

#### 6. **Documentation Helper**
- Navigate:  
  ```bash
  cd "Documentation Helper"
  ```
- Activate environment:  
  ```bash
  ./.venv/Scripts/activate
  ```
- Run (with Streamlit):  
  ```bash
  streamlit run main.py
  ```

---

#### 7. **Code Interpreter**
- Navigate:  
  ```bash
  cd "Code Interpreter"
  ```
- Activate environment:  
  ```bash
  ./.venv/Scripts/activate
  ```
- Run:  
  ```bash
  python main.py
  ```

---

### **Setting Up Pipenv for Multiple Subfolders with Isolated `.venv` Environments**

This is how to ensure that each subfolder has its own **Pipenv virtual environment** stored inside the subfolder (`.venv`), making it easy to distinguish environments. When activated, the environment name (same as the subfolder) will appear in parentheses before the terminal path.

---

#### **1. Remove Any Root-Level Pipenv Configuration (If Applicable)**  
If your root project folder contains a `Pipfile` or `Pipfile.lock`, Pipenv might try to associate all subfolders with the same virtual environment. To prevent this:
- **Delete** `Pipfile` and `Pipfile.lock` from the root manually.
- Or, if a virtual environment is already linked, remove it using:
  ```bash
  pipenv --rm
  ```

---

#### **2. Create a Separate Virtual Environment in Each Subfolder**  
Navigate to the subfolder where you want to create an isolated virtual environment and run:
```bash
cd ./subfoldername/
pipenv shell
```
This will:

✅ Create a **Pipfile** in that subfolder.  
✅ Create a `.venv` **inside** the subfolder to store dependencies.  
✅ Activate the virtual environment, displaying **(subfoldername)** before the path in the terminal.

If you want to **ensure the `.venv` is created inside the subfolder**, set:
```powershell
$env:PIPENV_VENV_IN_PROJECT = "1"
```
and then activate the pipenv shell:
```powershell
pipenv shell
```
Sometimes running the above 2 commands together works in creating the venv effectively.
```powershell
$env:PIPENV_VENV_IN_PROJECT = "1"
pipenv shell
```

#### **3. Activating the Virtual Environment in Any Subfolder**  
Once inside the subfolder, activate its virtual environment with:
```powershell
./.venv/Scripts/activate  # Windows (PowerShell)
```
This ensures the correct environment is used, and the terminal prompt should update to show `(subfoldername)` before the path.

---

#### **4. Switching Between Subfolder Environments**
1. **Deactivate the current environment** before switching:
   ```bash
   deactivate
   ```
2. **Navigate to another subfolder and activate its environment:**
   ```bash
   cd ../another-subfolder/
   ./.venv/Scripts/activate  # Windows
   ```

---

#### **5. Verify the Active Virtual Environment**
To confirm which virtual environment is currently active:
```powershell
pipenv --venv
```
This should return the path inside the current subfolder:
```
Folder Path\subfoldername\.venv
```

To further verify:
```powershell
echo $env:VIRTUAL_ENV  # PowerShell
```
This should match the `.venv` inside the current subfolder.

---

#### **6. Notes on Virtual Environment Naming**
- The environment name displayed in parentheses **before the path** (`(subfoldername)`) is auto-generated by Pipenv.
- If the folder name contains dashes (`-`), Pipenv may replace them with underscores (`_`), but the environment remains correct.

---

#### **7. Sometimes venv is not detected right**
- Sometimes some libraries even when venv is activated and the library is present in the `venv/lib` folder, it shows it can't find 
because the vscode ide is taking a different interpreter for the file.
- So, in that cases you have to enter: `ctrl + shift + p` and enter `Python: Select Interpreter` and then if you can't find the venv 
you are looking for: click on  `Enter Interpreter Path` and go to `.venv/Scripts/python.exe` in your folder where `.venv` is residing and  and choose `Select Interpreter` to resolve the issue

---

#### **Final Checklist**
✔ Each subfolder has its **own** `.venv` (not shared).  
✔ Activating the environment shows **(subfoldername)** before the terminal path.  
✔ `pipenv --venv` correctly displays the `.venv` path inside the subfolder.  
✔ Switching between environments works without conflicts.  

---

### 🧭 Why LangGraph?

When developing agents using **LangChain (ReAct)** or simple **LLM chaining**, there are a few major pain points:

- ❌ **Unreliable execution**  
- 🔁 Can end up in **infinite loops**  
- ⚠️ Prone to **errors** due to:
  - Ambiguous task definitions  
  - Poorly defined tools  
  - Over-flexibility (leaving too much to the LLM’s discretion)  

---

### 💡 The Problem

Relying **too much on the LLM** to figure out the next action or the sequence of steps introduces unpredictability.

As developers, we often **want control** — to define:

- 🛣️ The **flow** of the agent  
- 🔄 Whether cycles are allowed  
- ✅ How each tool is used  
- 🚫 What is **not allowed** during execution  

---

### 🔗 Enter: **LangGraph**

LangGraph solves these challenges by letting you build **agent workflows as graphs**, where:

- 🔹 **Nodes** = Actions, tools, or reasoning steps  
- 🔹 **Edges** = Controlled transitions between them  
- 🔁 You can define **cycles**, but with **full control**  
- 🎯 Enables **structured agent behavior** while still using LLMs for reasoning  

> 🧠 **LangGraph = Flexibility + Reliability** — A powerful combo for robust agent systems.

Check out the [LangGraph course on Udemy](https://www.udemy.com/course/langgraph/?couponCode=KEEPLEARNING) to dive deeper.
---

### Langsmith Setup

If you want to setup Langsmith tracing for your project, follow these steps:
1. Setup env variables:
    ```bash
    LANGCHAIN_TRACING_V2=true  # to start tracing
    LANGCHAIN_API_KEY = ""  # API Key created in Langsmith
    LANGCHAIN_PROJECT=Ice Breaker  # Project Name where you want tracing to happen
    ```
2. Load those environment variables in files where Agents are implemented (AgentExecutor) as vscode doesn't directly take env variables
3. Refer this documentation of setting up langsmith for more info: [Langmsith setting up](https://docs.smith.langchain.com/)
4. Benefits: 
    - You will be able to trace everything from initial prompt to tool outputs etc
    - You will get a fair idea about latency, cost etc
    - You can optimize quickly based on the information present there

---

### 📚 Resources for Building with LLMs

---

#### 1. 🔍 Prompt Library — *LangChain Hub*

Explore a wide variety of **battle-tested prompts** across use cases like:

- ✅ Entity extraction  
- 💬 SQL generation  
- 👨‍💻 Code generation  
- 📚 RAG pipelines  
- 🧠 Prompts optimized per LLM vendor (since prompts that work well on one model may not work on another)

→ Try them out and experiment here:  
👉 [LangChain Hub](https://smith.langchain.com/hub)

---

#### 2. 🧩 Text Chunking — *Text Splitter Playground*

When using **RAG**, it's crucial to chunk your text meaningfully so that:

- 📌 Each chunk retains context and meaning on its own  
- 📏 You choose the **right `chunk_size` and `chunk_overlap`**  
- 🧠 Chunks don’t lose semantics during retrieval

This is usually trial and error. But LangChain built a playground for this:  
👉 [Text Splitter Playground](https://langchain-text-splitter.streamlit.app/)

---

#### 3. 🆚 LlamaIndex vs LangChain

Both frameworks are used to build LLM applications. Here's a quick comparison:

| Feature            | **LlamaIndex**                | **LangChain**                  |
|--------------------|-------------------------------|--------------------------------|
| Focus              | Data-centric / RAG-heavy      | General-purpose LLM orchestration |
| RAG Capabilities   | 🔥 Very strong                 | ✅ Evolving and improving       |
| Tooling            | Great for structured data     | Great for agents + integrations |

You can choose based on your project’s needs — or combine them both!