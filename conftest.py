import pytest
from api_requests.characters import CharactersApi

def pytest_addoption(parser):
    parser.addoption("--login", action="store", help="description")
    parser.addoption("--password", action="store", help="description")

@pytest.fixture(scope="session")
def auth(request):
    login = request.config.getoption("login")
    password = request.config.getoption("password")

    return (login, password)

@pytest.fixture(scope="function")
def clear_storage(request):
    login = request.config.getoption("login")
    password = request.config.getoption("password")

    auth = (login, password)

    yield CharactersApi(auth).clear_storage()