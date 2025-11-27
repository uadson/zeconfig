def test_initial_defaults(config):
    assert config._ConfigGen__db_connection_string == "sqlite"
    assert config._ConfigGen__debug is True
    assert config._ConfigGen__db_name is None


def test_get_root_path_development_mode(temp_dev_env, config_dev):
    expected_root = temp_dev_env
    assert config_dev._ConfigGen__root_dir == expected_root
    assert config_dev._ConfigGen__root_dir.name == "project_root"


def test_get_root_path_installed_package_mode(mock_installed_package_env, config):
    expected_root = mock_installed_package_env
    assert config._ConfigGen__root_dir == expected_root
    assert config._ConfigGen__root_dir.name == "ze"


def test_get_envs_path_creates_dir(temp_dev_env, config):
    expected_env_path = temp_dev_env / "envs"
    assert config._ConfigGen__envs_dir == str(expected_env_path)
    assert expected_env_path.is_dir()


def test_get_envs_path_with_installed_package(config, tmp_path):
    config._ConfigGen__root_dir = tmp_path
    envs_path_str = config.get_envs_path()
    expected_envs_path = tmp_path / "envs"
    assert envs_path_str == str(expected_envs_path)
    assert expected_envs_path.is_dir()
