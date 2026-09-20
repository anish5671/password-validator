def is_valid_password(password):
    """Return True if password satisfies basic password requirements."""
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    return True


def has_special_character(password):
    """Return True if password contains at least one special character."""
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    return re.search(r"[^A-Za-z0-9]", password) is not None


def mask_password(password):
    """Return a masked version of a valid password."""
    if not is_valid_password(password):
        raise ValueError("password is not valid")

    return password[0] + "*" * (len(password) - 2) + password[-1]


def normalize_password(password):
    """Remove surrounding whitespace from a password."""
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    return password.strip()