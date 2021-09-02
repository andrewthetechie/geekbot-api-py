from typing import Dict
from typing import List
from typing import Optional

from pydantic import AnyUrl
from pydantic import BaseModel


class User(BaseModel):
    id: str
    email: str
    username: str
    realname: str
    profile_img: AnyUrl


class Team(BaseModel):
    id: int
    name: str
    users: List[User]


class Question(BaseModel):
    id: int
    color: str
    text: str
    schedule: Optional[str]
    answer_type: str
    answer_choices: List[Optional[str]]
    hasAnswers: bool
    is_random: bool
    random_texts: List[Optional[str]]
    prefilled_by: Optional[str]
    text_id: int
    preconditions: List[Optional[str]]
    label: str


class Standup(BaseModel):
    id: int
    name: str
    time: str
    wait_time: int
    timezone: str
    days: List[Optional[str]]
    channel: str
    channel_ready: bool
    questions: List[Question]
    users: List[User]
    users_total: int
    webhooks: List[Optional[str]]
    master: str
    sync_channel_members: bool


class Image(BaseModel):
    title: str
    image_url: AnyUrl


class Answer(BaseModel):
    id: int
    question: str
    question_id: str
    color: str
    answer: str
    images: List[Optional[Image]]


class Report(BaseModel):
    id: int
    slack_ts: str
    standup_id: str
    timestamp: int
    channel: str
    is_anonymous: bool
    member: User
    questions: List[Answer]


class AnswerIn(BaseModel):
    text: str


class ReportIn(BaseModel):
    standup_id: str
    answers: Dict[str, AnswerIn]
