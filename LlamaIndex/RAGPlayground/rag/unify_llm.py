from llama_index.llms.openai_like import OpenAILike
import os 
from typing import Any,Optional

class Unify(OpenAILike):
    def __init__(
        self,
        model: str,
        api_key: Optional[str] = None,
        api_base: str = "https://api.unify.ai/v0",
        is_chat_model: bool = True,
        **kwargs: Any,
    ) -> None:
        api_key = api_key or os.environ.get("UNIFY_API_KEY", None)
        super().__init__(
            model=model,
            api_key=api_key,
            api_base=api_base,
            is_chat_model=is_chat_model,
            **kwargs,
        )

    @classmethod
    def class_name(cls) -> str:
        """Get class name."""
        return "UnifyLLM"