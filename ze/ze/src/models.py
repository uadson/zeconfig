import importlib.resources as pkg_resources
import os
from pathlib import Path


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
        self.__root_dir: Path = self.get_root_path()
        self.__envs_dir = self.get_envs_path()

    @staticmethod
    def __set_root_path():
        root_package_name = __name__.split('.')[0]

        if root_package_name == '__main__':
            return Path(__file__).resolve().parent.parent
        else:
            return pkg_resources.files(root_package_name)

    def get_root_path(self):
        return self.__set_root_path()

    def __set_envs_path(self):
        envs_path = self.__root_dir / 'envs'
        os.makedirs(envs_path, exist_ok=True)
        return str(envs_path)

    def get_envs_path(self):
        return self.__set_envs_path()


config_gen = ConfigGen()
