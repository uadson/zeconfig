from pathlib import Path

from ze.src.core import initialize_project


def test_initialize_project_creates_files(monkeypatch, tmp_path: Path):
    """
    Tests if initialize_project correctly creates .env and settings.py
    in the current working directory.
    """
    # Altera o diretório de trabalho atual para o diretório temporário
    monkeypatch.chdir(tmp_path)

    # Executa a função principal que cria os arquivos
    initialize_project()

    # Verifica se os arquivos foram criados no diretório temporário
    env_file = tmp_path / ".env"
    settings_file = tmp_path / "settings.py"
    logger_file = tmp_path / "logger.py"

    assert env_file.exists(), ".env file was not created"
    assert settings_file.exists(), "settings.py file was not created"
    assert logger_file.exists(), "logger.py file was not created"

    # Verifica o conteúdo básico dos arquivos
    env_content = env_file.read_text()
    assert "DB_CONNECTION_STRING='sqlite'" in env_content
    assert "DB_NAME=" in env_content

    settings_content = settings_file.read_text()
    assert 'load_dotenv(".env")' in settings_content
    assert "DB_URL: str = f" in settings_content
