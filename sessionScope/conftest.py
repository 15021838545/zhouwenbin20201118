import pytest


@pytest.fixture(scope='session')
def login():
    print("前置")
    yield
    print("后置")