import tomli
from pathlib import Path


def set_package_version():
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    with open(BASE_DIR / "pyproject.toml", "rb") as f:
        data = tomli.load(f)
        version = data["project"]["version"]
        with open("version.py", "w") as f:
            f.write(f'VERSION = "{version}"')


if __name__ == "__main__":
    set_package_version()
