from src.indexer.chunker import chunk_code

def test_chunker():
    code = "line\n" * 120
    chunks = chunk_code(code, max_lines=50)
    assert len(chunks) == 3
