
import pytest

from app import time


def test_not_none_response():
    assert time() is not None


def test_if_string_response():
    assert type(time()) is str


def test_center_in_response():
    assert 'center' in time()