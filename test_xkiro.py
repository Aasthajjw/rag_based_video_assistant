
from dotenv import load_dotenv
load_dotenv()

from core.llm_client import get_llm

try:
    llm = get_llm()

    response = llm.invoke(
        "Explain artificial intelligence in three sentences."
    )

    print("\nXKIRO CONNECTION SUCCESSFUL!")
    print("\nResponse:")
    print(response.content)

except Exception as e:
    print("\nXKIRO CONNECTION FAILED!")
    print("Error:", str(e))
