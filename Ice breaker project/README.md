# Ice Breaker Project

Gist File Link for emulating an API Call to the ProxyCurl API: [Samudrala Santhosh Linkedin Profile](https://gist.githubusercontent.com/DCGUY009/16175ccc5daa5fa1a19b15ce9fba8044/raw/149bccd37bc0e359d60193ecc9074278c10d8161/gistfile1.txt)

Proxycurl API is used to fetch a person's social details such as Linkedin, Twitter, Facebook Profile and other details.

Tavily is a search API highly optimized for GenAI Workloads, it has a nice integration with Langchain.
It has the capability to search in Google, bing etc. But also, has the capability to figure out what to do based on the user query.
It is configured as a web search tool for Agents and it has a generous free tier which offers 1000 searches for month.
[Tavily API](https://app.tavily.com/home?code=0qIrwdD6-2w_5xcy_JMQSgFax71Cg0JNyHnqoEjPadFkf&state=eyJyZXR1cm5UbyI6Ii9ob21lIn0)

GIST For calling twitter API as it is limited and costly: [Twitter API Static Response - Santhosh]("https://gist.githubusercontent.com/DCGUY009/aea84135ed9d89f52683e971a2cd9c9a/raw/88bc968d6d425c3d339697520fcf116961704d6c/gistfile1.txt")


Update as of 27th Jan: Getting this error:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "D:\Genai_projects\Langchain - Develop LLM powered applications - Udemy Course\Ice breaker project\Agents\linkedin_lookup_agent.py", line 87, in <module>
    linkedin_url = lookup(name="Vaishnava Samudrala")
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Genai_projects\Langchain - Develop LLM powered applications - Udemy Course\Ice breaker project\Agents\linkedin_lookup_agent.py", line 63, in lookup
    agent_executor = AgentExecutor(
                     ^^^^^^^^^^^^^^
  File "C:\Users\Samudrala Santhosh\.virtualenvs\Ice_breaker-mc6Ks-e5\Lib\site-packages\langchain_core\load\serializable.py", line 125, in __init__
    super().__init__(*args, **kwargs)
  File "C:\Users\Samudrala Santhosh\.virtualenvs\Ice_breaker-mc6Ks-e5\Lib\site-packages\pydantic\main.py", line 214, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 1 validation error for AgentExecutor
agent
  Field required [type=missing, input_value={'api_key': 'lsv2_pt_6aee...FC0>)], 'verbose': True}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing