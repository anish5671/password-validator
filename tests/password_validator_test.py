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

    assert result == "S*******3"


def test_password_missing_uppercase():
    """Test that passwords without uppercase are rejected."""
    assert is_valid_password("secure123") == False


def test_password_missing_lowercase():
    """Test that passwords without lowercase are rejected."""
    assert is_valid_password("SECURE123") == False


def test_password_missing_digit():
    """Test that passwords without digit are rejected."""
    assert is_valid_password("SecureABC") == False


def test_mask_password_invalid():
    """Test masking an invalid password raises ValueError."""
    with pytest.raises(ValueError):
        mask_password("short")


def test_has_special_character():
    """Test detection of special characters."""
    assert has_special_character("Secure123!") == True
    assert has_special_character("Secure123") == False


def test_has_special_character_type_error():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError):
        has_special_character(12345678)


def test_normalize_password():
    """Test surrounding whitespace is removed."""
    assert normalize_password("  Secure123  ") == "Secure123"


def test_normalize_password_type_error():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError):
        normalize_password(None)
