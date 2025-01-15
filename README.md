# Template Python Docker

This template provides a minimal Docker configuration for Python projects, with a clear and reproducible project structure.

## Project Structure

Below is the template structure. **Note: The `.py` files in `tests/`, `scripts/`, and `module/` directories are provided as examples and should be replaced with your own code.**

```
project/
│
├── src/                    # Main source code
│   ├── module/            # Reusable Python modules
│   │   ├── matrix.py      # (example)
│   │   └── hello_world.py # (example)
│   ├── scripts/           # Executable scripts
│   │   └── my_script.py   # (example)
│   └── requirements.txt   # Project dependencies
│
├── tests/                 # Unit tests
│   ├── __init__.py
│   ├── conftest.py       # pytest configuration
│   ├── test_matrix.py    # (example)
│   └── test_hello_world.py # (example)
│
└── Dockerfile            # Docker configuration
```

## Prerequisites

- Python installed on your development machine
- pipreqs installed: `pip install pipreqs`
- pytest and pytest-cov for testing and coverage:
  ```bash
  pip install pytest
  pip install pytest-cov
  ```
  or in one command:
  ```bash
  pip install pytest pytest-cov
  ```

## Using the Template

To use this template without Git history, you have three options:

1. Via GitHub interface:
   - Click on the green "Use this template" button
   - Choose "Create a new repository"
   - Or "Download ZIP" to download without creating a repository

2. Via command line with Git:
```bash
git clone --depth 1 https://github.com/ID2L/template-python-docker.git my_project
cd my_project
rm -rf .git
git init
```

3. Via wget:
```bash
wget https://github.com/ID2L/template-python-docker/archive/refs/heads/main.zip -O template.zip
unzip template.zip
mv template-python-docker-main/* .
rm -rf template-python-docker-main template.zip
```

## Code Organization

### Module

The `src/module/` directory contains reusable Python modules. For example:
- `matrix.py`: Implementation of matrix functions
- `hello_world.py`: Simple module example

### Scripts

The `src/scripts/` directory contains executable scripts that use the modules.

## Using Docker

1. Building the image:
```bash
docker build -t my_python_app .
```

2. Running the container:
```bash
docker run -it my_python_app
```

## Dependencies Management

To automatically generate the `requirements.txt` file from your code:

```bash
pipreqs --force src/
```

This command will:
- Analyze all Python files in your project src folder
- Identify all used dependencies
- Create or update the `requirements.txt` file

## Tests

### Test Structure

Tests are placed in the `tests/` directory. The recommended structure is:

```
tests/
├── __init__.py           # Makes tests directory importable
├── conftest.py          # pytest configuration (shared fixtures)
├── test_matrix.py       # Tests for matrix.py
└── test_hello_world.py  # Tests for hello_world.py
```

### Running Tests

To run the tests:

```bash
# Run all tests
pytest

# Run tests with more details
pytest -v

# Run a specific test file
pytest tests/test_matrix.py
```

### Code Coverage

To generate a code coverage report:

```bash
# Generate a terminal report
pytest --cov=src tests/

# Generate a detailed HTML report
pytest --cov=src --cov-report=html tests/
```

The HTML report will be generated in the `htmlcov/` directory. Open `htmlcov/index.html` in your browser to view the results.

## For More Information

- [Official pytest documentation](https://docs.pytest.org/)
- [pytest-cov documentation](https://pytest-cov.readthedocs.io/)
