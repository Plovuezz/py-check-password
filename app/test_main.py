import pytest
from .main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Passw@rd1", True),
        ("qwerty", False),
        ("Qw@rty1", False),
        ("Passw@rd1password", False),
        ("a1@     ", False),
        ("     a1@", False),
        ("passw@rd1", False),
        ("Password1", False),
        ("Passw@rdd", False),
    ],
    ids=[
        "regular case",
        "short password",
        "short with uppercase symbol and letter",
        "too long password",
        "password with too many spaces",
        "password with too many spaces v2",
        "password with no uppercase",
        "password with no symbol",
        "password with no letter",
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result