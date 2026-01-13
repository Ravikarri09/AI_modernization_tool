import click
from src.indexer.indexer import index_codebase
from src.retrieval.search import search_code

@click.group()
def cli():
    pass

@cli.command()
@click.argument("path")
def index(path):
    """Index a legacy codebase"""
    index_codebase(path)

@cli.command()
@click.argument("query")
def search(query):
    """Search code semantically"""
    results = search_code(query)
    for r in results:
        print(r)

if __name__ == "__main__":
    cli()
