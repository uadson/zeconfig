import typer
from core import get_root_path
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def init(
    mode: str = typer.Argument('default', help='Modo de execução padrão.'),
    verbose: bool = typer.Option(False, '--verbose', '-v', help='Exibe logs detalhados.'),
):
    """
    Cria variáveis de configuração padrão.
    """
    print('Executando a funcionalidade padrão...')
    print(f'Modo escolhido: {mode}')
    console.print(f'Obtendo o caminho do diretório raiz: {get_root_path()}')

    if verbose:
        print('[LOG] Verbose ativado: Carregando módulos extras...')


@app.command()
def django():
    """
    Estrutura de configurações para o Django
    """
    print('Carregando configurações para o Django...')


@app.command()
def fastapi():
    """
    Estrutura de configurações para o FastAPI
    """
    print('Carregando configurações para o FastAPI...')


def main():
    app()
