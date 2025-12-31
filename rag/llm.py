from llama_index.llms.ollama import Ollama

def get_llm():
    return Ollama(
        model="llama3",
        temperature=0
    )
