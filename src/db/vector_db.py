import lancedb

db = lancedb.connect("./vector_store")

def store_embedding(file, chunk, embedding):
    table = db.create_table("code_embeddings", 
        data=[{
            "file": file,
            "content": chunk,
            "embedding": embedding
        }],
        mode="append"
    )
