import pytest
from src.password_validator import (
    is_valid_password,
    has_special_character,
    mask_password,
    normalize_password,
)


def test_valid_password():
    """Test a valid password."""
    password = "Secure123"

    result = is_valid_password(password)

    assert result == True


def test_short_password():
    """Test that passwords shorter than 8 characters are rejected."""
    password = "Ab12"

    result = is_valid_password(password)

    assert result == False


def test_password_type_error():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_password(12345678)


def test_mask_password():
    """Test masking a valid password."""
    password = "Secure123"

    result = mask_password(password)

    assert result == "S****1"