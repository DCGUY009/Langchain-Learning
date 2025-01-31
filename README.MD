## This is me learning, unlearning and relearning Langchain from Eden Marco's Udemy Course

Course Link - [LangChain- Develop LLM powered applications with LangChain](https://www.udemy.com/course/langchain/?couponCode=KEEPLEARNING)



### Instructions for Setting Up a Pipenv with Multiple Subfolders:

1. **If you have multiple subfolders with their own `pipenv` and isolated environments** (and not using the root folder for anything):
   - **Delete the `Pipfile` and `Pipfile.lock` in the root folder**. This will prevent `pipenv` from associating any virtual environment with the root folder when you create environments in the subfolders. You can delete these files manually or use `pipenv --rm` to remove the virtual environment if one exists in the root.

2. **Navigate to the subfolder** where you want to create a new `pipenv` environment:
   ```bash
   cd ./subfoldername/
   ```
3. **Create a new** `Pipfile` **and virtual environment** in that subfolder:
    ```bash
    pipenv shell
    ```
    This will create both a `Pipfile` and a virtual environment for that subfolder.

4. **If the wrong virtual environment** appears in the parentheses before the path (showing the environment from a different subfolder or root folder):
    - This is usually because the terminal prompt didn’t update after you created the new environment.
    - Relaunch the terminal to reset the environment.

5. **After relaunching the terminal:**

    - Navigate back to the subfolder and check the virtual environment using:

    ```bash
    pipenv --venv
    ```
    - This command will display the absolute path of the current virtual environment.
    - You can also check the VIRTUAL_ENV environment variable to confirm the active virtual environment:

    ```bash
    echo $env:VIRTUAL_ENV  # For PowerShell
    ```
6. **Verify that the correct virtual environment is activated:**
    - When you check the virtual environment path, ensure that it matches the path shown by `pipenv --venv`.
    - The environment name in the parentheses before the path should be consistent with the virtual environment's path after running `pipenv --venv`.

7. **Note on the virtual environment name:**
    The environment name displayed in the parentheses (before the path) may show a cleaned-up version of the name (e.g., replacing dashes - with underscores _). This is to avoid naming errors. However, both the cleaned-up version and the path are pointing to the same virtual environment.



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
