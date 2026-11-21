
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()


def get_llm():
    """
    Creates an LLM connection through XKIRO's
    OpenAI-compatible API.
    """

    api_key = os.getenv("XKIRO_API_KEY")

    if not api_key:
        raise ValueError(
            "XKIRO_API_KEY is missing. "
            "Please add it to your .env file."
        )

    return ChatOpenAI(
        model="mistralai/mistral-large-2512",
        api_key=api_key,
        base_url="https://api.xkiro.com/v1",
        temperature=0.3,
        max_tokens=2048,
    )
