from langchain.callbacks.base import BaseCallbackHandler
from typing import Dict, Any, List
from langchain.schema import (
    LLMResult,
)  # Most of this imports are not known commonly, would get more idea once more projects are done


class AgentCallBackHandler(BaseCallbackHandler):
    # We are overriding the custom on_llm_start and on_llm_end methods and implementing our custom logic here
    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        """Run when LLM starts running"""
        print(f"***Prompt to LLM was: ***\n{prompts[0]}")
        print("***********")

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        """Run when LLM ends running"""
        print(f"***LLM Response: ***\n{response.generations[0][0].text}")
        print("***********")
