"""
Pytest configuration file.
This file can contain fixtures and other test configurations.
"""

import pytest

@pytest.fixture
def sample_name():
    """Fixture providing a sample name for testing."""
    return "John"

@pytest.fixture
def empty_name():
    """Fixture providing an empty name for testing."""
    return ""