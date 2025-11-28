import os
import sys
from unittest.mock import patch

import pytest

# Adiciona o diretório src ao sys.path para permitir a importação do models
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../ze/src')))

from models import ConfigGen


@pytest.fixture
def mock_pkg_resources(tmp_path):
    """Fixture para mockar importlib.resources.files e __name__."""
    # Cria um diretório 'ze' para simular a estrutura do pacote
    package_dir = tmp_path / 'ze'
    package_dir.mkdir()
    (package_dir / '__init__.py').touch()

    with patch('importlib.resources.files', return_value=package_dir) as mock_files:
        with patch('models.__name__', 'ze.src.models'):
            yield mock_files, package_dir


def test_configgen_initialization(mock_pkg_resources):
    """Testa se a inicialização de ConfigGen cria o diretório 'envs'."""
    _, package_dir = mock_pkg_resources
    ConfigGen()
    assert (package_dir / 'envs').is_dir()


def test_create_envfile_default(mock_pkg_resources):
    """Testa a criação do arquivo .env padrão."""
    _, package_dir = mock_pkg_resources
    cg = ConfigGen()
    cg.create_envfile_default()
    env_file = package_dir / '.env'
    assert env_file.is_file()
    content = env_file.read_text()
    assert "DB_CONNECTION_STRING='sqlite'" in content
    assert 'DB_NAME=' in content
