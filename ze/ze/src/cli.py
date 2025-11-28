import typer
from rich.console import Console

from . import core


app = typer.Typer()
console = Console()


@app.command()
def init(
    mode: str = typer.Argument("default", help="Default Mode."),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose output."),
):
    """
    Create a .env, settings.py and logger.py files in the current working directory
    """
    if mode == "default":
        core.initialize_project()
    else:
        console.print(
            f"[yellow]Mode '{mode}' not recognized. Using 'default'.[/yellow]"
        )
        core.initialize_project()


@app.command()
def fastapi(
    mode: str = typer.Argument("FastAPI", help="FastAPI Mode."),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose output."),
):
    """
    Create a .env, settings.py files in the current working directory
    """
    if mode == "FastAPI":
        core.initialize_fastapi_project()
    else:
        console.print(
            f"[yellow]Mode '{mode}' not recognized. Using 'FastAPI'.[/yellow]"
        )
        core.initialize_fastapi_project()


@app.command()
def version():
    """
    Returns the version of the package.
    """
    core.get_package_version()


def main():
    app()
