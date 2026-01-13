import lancedb

db = lancedb.connect("./vector_store")

def search_code(query):
    table = db.open_table("code_embeddings")
    results = table.search(query).limit(5).to_list()

    return results
