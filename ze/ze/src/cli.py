import typer
from rich.console import Console

from .core import initialize_project

app = typer.Typer()
console = Console()


@app.command()
def init(
    mode: str = typer.Argument("default", help="Default mode."),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose output."),
):
    """
    Create a .env, settings.py and logger.py files in the current working directory
    """
    if mode == "default":
        initialize_project()
    else:
        console.print(
            f"[yellow]Mode '{mode}' not recognized. Using 'default'.[/yellow]"
        )
        initialize_project()


@app.command()
def django():
    """
    Estrutura de configurações para o Django
    """
    print("Carregando configurações para o Django...")


@app.command()
def fastapi():
    """
    Estrutura de configurações para o FastAPI
    """
    print("Carregando configurações para o FastAPI...")


def main():
    app()
