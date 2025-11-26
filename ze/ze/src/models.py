import json
import os
import pathlib

import yaml

try:
    import tomllib
except ImportError:
    import tomli as tomllib
from abc import ABC, abstractmethod


class ConfigParser(ABC):
    """
    Abstract base class for configuration
    file parses.
    """

    @abstractmethod
    def parse(self, file_path: str) -> dict:
        """
        Parses a configuration file.

        Args:
            file_path (str): Path to the
            configuration file.

        Returns:
            dict: Parsed configuration data.
        """


class JSONParser(ConfigParser):
    @classmethod
    def parse(cls, file_path: str) -> dict:
        """
        Parses a JSON configuration file.

        Args:
            file_path: The path to the JSON file.

        Returns:
            A dictionary containing the parsed JSON data.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)


class TOMLParser(ConfigParser):
    @classmethod
    def parse(cls, file_path: str) -> dict:
        """
        Parses a TOML configuration file.

        Args:
            file_path: The path to the TOML file.

        Returns:
            A dictionary containing the parsed TOML data.
        """
        with open(file_path, 'rb') as file:
            return tomllib.load(file)


class YAMLParser(ConfigParser):
    @classmethod
    def parse(cls, file_path: str) -> dict:
        """
        Parses a YAML configuration file.

        Args:
            file_path: The path to the YAML file.

        Returns:
            A dictionary containing the parsed YAML data.
        """
        with open(file_path, 'rb') as file:
            return yaml.safe_load(file)


class ENVParser(ConfigParser):
    @classmethod
    def parse(cls, file_path: str) -> dict:
        """
        Parses a .env configuration file.

        Args:
            file_path: The path to the .env file.

        Returns:
            A dictionary containing the parsed environment variables.
        """
        config = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            for default_line in file:
                line = default_line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    config[key] = value
        return config


class ConfigGen:
    def __init__(self):
        self.__db_connection_string: str = 'sqlite'
        self.__db_name: str = None
        self.__db_user: str = None
        self.__db_password: str = None
        self.__db_host: str = None
        self.__db_port: str = None
        self.__secret_key: str = None
        self.__allowed_hosts: list = None
        self.__debug: bool = True
        self.__root_dir = (
            pathlib.Path(__file__).resolve().parent.parent.parent.parent.parent.parent.parent
        )  # /root/.venv/lib/python3.xx/site-packages/ze/src
        self.__envs_dir = self.__get_envs_dir()

    def __get_envs_dir(self):
        os.makedirs(os.path.join(self.__root_dir, 'envs'), exist_ok=True)
        return os.path.join(self.__root_dir, 'envs')


if __name__ == '__main__':
    config = ConfigGen().root_dir
    print(config)
