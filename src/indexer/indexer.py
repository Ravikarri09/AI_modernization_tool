from src.indexer.file_scanner import scan_files
from src.indexer.chunker import chunk_code
from src.llm.ollama import get_embedding
from src.db.vector_db import store_embedding

def index_codebase(path):
    files = scan_files(path)
    print(f"Indexing {len(files)} files...")

    for file in files:
        try:
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            chunks = chunk_code(content)

            for chunk in chunks:
                embedding = get_embedding(chunk)
                store_embedding(file, chunk, embedding)

            print(f"Indexed: {file}")
        except Exception as e:
            print(f"Failed: {file} -> {e}")

    print("Indexing complete.")
