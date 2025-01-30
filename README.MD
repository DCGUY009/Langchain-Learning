## This is me learning, unlearning and relearning Langchain from Eden Marco's Udemy Course

Course Link - [LangChain- Develop LLM powered applications with LangChain](https://www.udemy.com/course/langchain/?couponCode=KEEPLEARNING)

If you want to setup Langsmith tracing for your project, follow these steps:
1. Setup env variables:
    - LANGCHAIN_TRACING_V2=true  # to start tracing
    - LANGCHAIN_API_KEY = ""  # API Key created in Langsmith
    - LANGCHAIN_PROJECT=Ice Breaker  # Project Name where you want tracing to happen
2. Load those environment variables in files where Agents are implemented (AgentExecutor) as vscode doesn't directly take env variables
3. Refer this documentation of setting up langsmith for more info: (Langmsith setting up)[https://docs.smith.langchain.com/]
4. Benefits: 
    - You will be able to trace everything from initial prompt to tool outputs etc
    - You will get a fair idea about latency, cost etc
    - You can optimize quickly based on the information present there
