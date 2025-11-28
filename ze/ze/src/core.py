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
