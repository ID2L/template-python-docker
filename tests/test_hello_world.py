"""
Test module for my_module.py
"""

import pytest
from src.module.hello_world import hello_world


def test_hello_world(sample_name):
    """Test the hello_world function with a sample name from fixture."""
    # Given
    expected = f"Hello World {sample_name}"

    # When
    result = hello_world(sample_name)

    # Then
    assert result == expected


def test_hello_world_empty_string(empty_name):
    """Test the hello_world function with an empty string from fixture."""
    # Given
    expected = "Hello World "

    # When
    result = hello_world(empty_name)

    # Then
    assert result == expected
