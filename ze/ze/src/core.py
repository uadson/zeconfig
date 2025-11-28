import tomli
from pathlib import Path
from rich.console import Console

from .models import ConfigGen

console = Console()


def initialize_project():
    """
    Initializes the project by creating default .env, settings.py and logger.py files.
    """
    try:
        config_generator = ConfigGen()
        console.print(
            "[bold green]Creating default configuration files...[/bold green]"
        )
        config_generator.create_files_default()
        console.print(
            "\n[bold blue]Configuration files .env, settings.py and logger.py created successfully![/bold blue]"
        )
    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}[/bold red]")


def initialize_fastapi_project():
    """
    Initializes the project by creating .env, settings.py and logger.py files.
    """
    try:
        config_generator = ConfigGen()
        console.print(
            "[bold green]Creating fastapi configuration files...[/bold green]"
        )
        config_generator.create_fastapi_files()
        console.print(
            "\n[bold blue]Configuration files .env, settings.py and created successfully![/bold blue]"
        )
    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}[/bold red]")


def get_package_version():
    """
    Returns the version of the package.
    """
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    with open(BASE_DIR / "pyproject.toml", "rb") as f:
        data = tomli.load(f)
        console.print(f"[bold blue]Version: {data['project']['version']}[/bold blue]")
