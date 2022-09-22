import pytest


def always_returns_true():
    print("we are making some issues happen!")
    return None


def test_always_returns_true():
    assert always_returns_true()
