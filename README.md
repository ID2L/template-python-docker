# Template Python Docker

This template provides a minimal Docker configuration for your Python projects.

## Prerequisites

- Python installed on your development machine
- pipreqs installed: `pip install pipreqs`
- pytest and pytest-cov for testing: `pip install pytest pytest-cov`

## Template Download

To use this template without Git history, you have three options:

1. Via GitHub interface:
   - Click on the green "Use this template" button
   - Choose "Create a new repository"
   - Or "Download ZIP" to download without creating a repository

2. Via command line with Git:
```bash
mv .git .git_tmp
git clone --depth 1 https://github.com/ID2L/template-python-docker.git .
rm -rf .git
mv .git_tmp .git
```

3. Via wget:
```bash
wget https://github.com/ID2L/template-python-docker/archive/refs/heads/main.zip -O template.zip
unzip template.zip
mv template-python-docker-main/* .
rm -rf template-python-docker-main template.zip
```

## Using the Dockerfile

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
- Analyze all Python files in your project
- Identify all used dependencies
- Create or update the `requirements.txt` file

> Note: The `--force` option allows overwriting the requirements.txt file if it already exists.

## Tests

### Test Structure

Tests should be placed in the `tests/` directory. Here's a recommended structure:

```
project/
│
├── src/
│   └── my_module.py
│
└── tests/
    ├── __init__.py
    ├── test_my_module.py
    └── conftest.py  # pytest configuration file (optional)
```

### Running Tests

To run the tests:

```bash
# Run all tests
pytest

# Run tests with more details
pytest -v

# Run a specific test file
pytest tests/test_my_module.py
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

For more information, visit:
- [Official pytest documentation](https://docs.pytest.org/)
- [pytest-cov documentation](https://pytest-cov.readthedocs.io/)
