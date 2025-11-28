# ZeConfig [EN](README.md)   -   [BR](README_BR.md)
[![Buid](https://github.com/uadson/zeconfig/actions/workflows/zconf-build.yml/badge.svg)](https://github.com/uadson/zeconfig/actions/workflows/zconf-build.yml)
[![Tests](https://github.com/uadson/ZeConfig/actions/workflows/zconf-tests.yml/badge.svg)](https://github.com/uadson/ZeConfig/actions/workflows/zconf-tests.yml)
[![Release](https://github.com/uadson/zeconfig/actions/workflows/release.yml/badge.svg)](https://github.com/uadson/zeconfig/actions/workflows/release.yml)

<p align="center">
  <img src="https://github.com/user-attachments/assets/be41acda-3565-477a-9886-8944b6af9573" alt="ZeConfig" width="600">
</p>

ZeConfig is a Python library designed to manage application settings, making it easy to handle sensitive data and environment-specific configurations. It supports configuration files in TOM, JSON, YAML, YML, and ENV formats.

## Features

- **Automatic Detection**: Automatically finds the configuration file within the current directory or its subdirectories.
- **Multi-format Support**: Works seamlessly with TOML, JSON, YAML, YML, and ENV files.
- **Simple API**: Easy access to keys and values for any environment.

## Installation

```bash
pip install zeconfig
```

## How to Use

### 1. Create a Configuration File

In your project's root directory, create a configuration file. For example, a `config.json`:

```json
{
    "DATABASE_URL":  "sqlite:///dev.db",
    "SECRET_KEY": "a-very-secret-key"
}
```

Or a `.env` file:

```env
DATABASE_URL="sqlite:///dev.db"
SECRET_KEY="a-very-secret-key"
```

### 2. Initialize ZeConfig

In your Python code, just import `config` from the `ze` library.

```python
from ze import config
```

### 3. Access Your Settings

Retrieve any value by its key. ZeConfig will automatically load it from your configuration file.

```python
DATABASE_URL = config("DATABASE_URL")
SECRET_KEY = config("SECRET_KEY")

print(f"Database URL: {DATABASE_URL}")

>>> OUTPUT: 
    Database URL: sqlite:///dev.db
```

## Error Handling

ZeConfig raises descriptive exceptions for common issues:

- `FileNotFoundError`: If no configuration file is found in the project.
- `KeyError`: If a requested key is missing from the configuration file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request on the GitHub repository.