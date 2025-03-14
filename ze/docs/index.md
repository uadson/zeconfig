# ZeConfig [EN](index.md)   -   [BR](index_br.md)
[![Buid](https://github.com/uadson/zeconfig/actions/workflows/zconf-build.yml/badge.svg)](https://github.com/uadson/zeconfig/actions/workflows/zconf-build.yml)
[![Tests](https://github.com/uadson/zeconfig/actions/workflows/zconf-tests.yml/badge.svg)](https://github.com/uadson/zeconfig/actions/workflows/zconf-tests.yml)
[![Release](https://github.com/uadson/zeconfig/actions/workflows/release.yml/badge.svg)](https://github.com/uadson/zeconfig/actions/workflows/release.yml)



<p align="center">
  <img src="https://github.com/user-attachments/assets/be41acda-3565-477a-9886-8944b6af9573" alt="ZeConfig" width="600">
</p>

ZeConfig is a Python library designed to manage application configurations, making it easier to handle sensitive data and environment-specific settings. It supports configuration files in both TOM, JSON, YAML, YML and ENV formats.

## Features

- Automatic detection of configuration file location within the current directory or its subdirectories.
- Support for TOML, JSON, YAML, YML and ENV configuration files.
- Easy access to environment-specific keys and values.

## Installation

```bash
pip install zeconfig
```

## Usage

### 0. Creating a configuration file
At the root of the project, create a file with one of the extensions .toml, .json, .yaml, .yml or .env.

For example: config.json

### 1. Configuration File Format

### Example `config.json`

```json
{
    "DATABASE_URL":  "sqlite:///dev.db",
    "SECRET_KEY": "dev-secret"
}
```

### 2. Initialize ZeConfig

```python
from ze import config
```

### 3. Manage Environment Settings

Retrieve a value for a specific key in the current environment:

```python
DATABASE_URL = config("DATABASE_URL")
print(f"Database URL: {DATABASE_URL}")

>>> OUTPUT: 
    sqlite:///dev.db
```

## Error Handling

ZeConfig raises descriptive exceptions for common issues:


- `KeyError`: Missing environment or key in the configuration file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on the [GitHub repository](https://github.com/uadson/zeconfig).

## Contact

For questions or support, please reach out to [uadsonpy@gmail.com](mailto:uadsonpy@gmail.com).
