import pytest

from geekbot_api.client import GeekbotAPIClient
from geekbot_api.config import GeekbotAPIConfig
from geekbot_api.schemas import Question
from geekbot_api.schemas import Answer
from geekbot_api.schemas import Standup
from geekbot_api.schemas import Team
from geekbot_api.schemas import User
from geekbot_api.schemas import Report
from pydantic import parse_obj_as, HttpUrl


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
def fake_user():
    yield User(id="0",
               email="test@test.com",
               username="testuser",
               realname="Testy McTest",
               profile_img=parse_obj_as(HttpUrl,
                                        "http://fakeimg.com/fake.png"))


@pytest.fixture()
def fake_team(fake_user):
    """Sets up a fake team object"""
    yield Team(
        id=0,
        name="TestTeam",
        users=[fake_user],
    )


@pytest.fixture()
def fake_question():
    yield Question(
        id=0,
        color="blue",
        text="Test question",
        schedule=None,
        answer_type="test",
        answer_choices=list(),
        hasAnswers=False,
        is_random=False,
        random_texts=list(),
        prefilled_by=None,
        text_id=0,
        preconditions=list(),
        label="test",
    )


@pytest.fixture()
def fake_standup(fake_user, fake_question):
    """Sets up a fake team object"""
    yield Standup(
        id=0,
        channel_ready=False,
        sync_channel_members=False,
        users_total=3,
        master="test",
        webhooks=list(),
        name="test",
        time="09:00:00",
        wait_time=0,
        timezone="UTC",
        days=["Monday"],
        channel="testchannel",
        questions=[fake_question],
        users=[fake_user],
        personalized=False,
    )


@pytest.fixture()
def fake_answer():
    yield Answer(id=1,
                 question="What's on your mind today?",
                 question_id='12345',
                 color='e37979',
                 answer="spring, summer and fall",
                 images=[])


@pytest.fixture()
def fake_report(fake_user, fake_answer):
    """Sets up a fake report object"""
    yield Report(id=0,
                 slack_ts="0",
                 standup_id="standup-1",
                 timestamp=0,
                 channel="testchannel",
                 is_anonymous=True,
                 member=fake_user,
                 questions=[fake_answer])
