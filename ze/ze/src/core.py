from models import ConfigGen
from rich.console import Console

console = Console()


def initialize_project():
    """
    Initializes the project by creating default .env and settings.py files.
    """
    try:
        config_generator = ConfigGen()
        console.print("[bold green]Creating default .env file...[/bold green]")
        config_generator.create_envfile_default()
        console.print("[bold green]Creating default settings.py file...[/bold green]")
        config_generator.create_settings_default()
        console.print(
            "\n[bold blue]Configuration files created successfully![/bold blue]"
        )
    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}[/bold red]")
