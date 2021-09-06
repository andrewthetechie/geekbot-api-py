import pytest

from geekbot_api.client import GeekbotAPIClient
from geekbot_api.config import GeekbotAPIConfig
from geekbot_api.schemas import Team
from geekbot_api.schemas import User


@pytest.fixture()
def test_client(requests_mock):
    """Sets up a client we can use"""
    config = GeekbotAPIConfig(api_key="api_testkey")
    client = GeekbotAPIClient(config=config)
    yield {"config": config, "client": client, "requests_mock": requests_mock}


@pytest.fixture()
def test_async_client(httpx_mock):
    """Sets up a client we can use"""
    config = GeekbotAPIConfig(api_key="api_testkey")
    client = GeekbotAPIClient(config=config)
    yield {"config": config, "client": client, "httpx_mock": httpx_mock}


@pytest.fixture()
def fake_team():
    """Sets up a fake team object"""
    yield Team(
        id=0,
        name="TestTeam",
        users=[
            User(
                id=0,
                email="test@test.com",
                username="testuser",
                realname="Testy McTest",
                profile_img="http://fakeimg.com/fake.png",
            )
        ],
    )
