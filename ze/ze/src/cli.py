import typer

from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def run(
    mode: str = typer.Argument(
        "default", help="O modo de execução: (ex: django, fastapi)."
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Exibe logs detalhados."
    ),
):
    """
    Executa a funcionalidade principal do pacote.
    """
    print("Executando a funcionalidade principal...")
    print(f"Modo escolhido: {mode}")

    if verbose:
        print("[LOG] Verbose ativado: Carregando módulos extras...")


@app.command()
def version():
    """
    Exibe a versão atual do pacote
    """
    print("Packege v...")


if __name__ == "__main__":
    app()
