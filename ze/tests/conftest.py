from unittest.mock import MagicMock

import pytest

from ze.src.models import ConfigGen


@pytest.fixture
def config():
    return ConfigGen()


@pytest.fixture
def config_dev():
    return ConfigGen()


@pytest.fixture
def mock_installed_package_env(monkeypatch, tmp_path):
    PACKAGE_NAME = 'ze'
    MOCKED_ROOT_PATH = tmp_path / 'site-packages' / PACKAGE_NAME
    MOCKED_ROOT_PATH.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr('ze.src.models.__name__', f'{PACKAGE_NAME}.src.models')

    mock_pkg_resources = MagicMock()
    mock_pkg_resources.files.return_value = MOCKED_ROOT_PATH

    monkeypatch.setattr('ze.src.models.pkg_resources', mock_pkg_resources)

    return MOCKED_ROOT_PATH


@pytest.fixture
def temp_dev_env(tmp_path, monkeypatch):
    dev_root = tmp_path / 'project_root'
    src_dir = dev_root / 'src'
    src_dir.mkdir(parents=True, exist_ok=True)

    mock_file_path = src_dir / 'models.py'
    monkeypatch.setattr('ze.src.models.__file__', str(mock_file_path))
    monkeypatch.setattr('ze.src.models.__name__', '__main__')

    return dev_root
