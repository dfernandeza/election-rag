from llama_index.core import SimpleDirectoryReader

def load_pdfs(path: str):
    return SimpleDirectoryReader(
        input_dir=path,
        recursive=True
    ).load_data()
