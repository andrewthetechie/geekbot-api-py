from abc import ABCMeta
from functools import lru_cache
from typing import Dict
from typing import List
from typing import Optional

import httpx
from httpx import Response
from pydantic import AnyUrl

from .config import GeekbotAPIConfig
from .schemas import AnswerIn
from .schemas import Report
from .schemas import ReportIn
from .schemas import Standup
from .schemas import Team


class _AbstractClient(metaclass=ABCMeta):
    def __init__(
        self,
        base_api_path: AnyUrl,
        api_version: str,
        path: str,
        api_key: str,
        headers: Optional[Dict] = {},
    ):
        self.api_path = f"{base_api_path}/{api_version}/{path}"
        self.headers = headers
        self.headers["Authorization"] = api_key
        self.headers["user-agent"] = self.headers.get(
            "user-agent", "geekbot-api-pi/0.1.0"
        )

    async def _http_get(self, path: str = "") -> Response:
        """Does a get against the geekbot api, adds "path" to the end of self.api_path"""
        async with httpx.AsyncClient() as client:
            r = await client.get(self._get_request_path(path), headers=self.headers)
        return r

    async def _http_put(self, data: Dict, path: str = "") -> Response:
        """Does a put against the geekbot api, adds "path" to the end of self.api_path"""
        async with httpx.AsyncClient() as client:
            r = await client.put(
                self._get_request_path(path), data=data, headers=self.headers
            )
        return r

    async def _http_post(self, data: Dict, path: str = "") -> Response:
        """Does a post against the geekbot api, adds "path" to the end of self.api_path"""
        async with httpx.AsyncClient() as client:
            r = await client.post(
                self._get_request_path(path), data=data, headers=self.headers
            )
        return r

    async def _http_delete(self, path: str) -> Response:
        """Does a post against the geekbot api, adds "path" to the end of self.api_path"""
        async with httpx.AsyncClient() as client:
            r = await client.delete(self._get_request_path(path), headers=self.headers)
        return r

    @lru_cache
    def _get_request_path(self, path: str = "") -> str:
        """combines self.api_path and a path string into a request path"""
        return f"{self.api_path}/{path}" if path != "" else self.api_path

    def __hash__(self):
        return hash(f"{self.api_path}-{type(self).__name__}")


class _TeamClient(_AbstractClient):
    async def list(self):
        """Gets teams and yields them as a generator"""
        response = await self._http_get()
        response_json = response.json()
        if type(response_json) is List:
            for team in response_json:
                yield Team(**team)
        else:
            yield Team(**response_json)


class _ReportClient(_AbstractClient):
    async def create(self, standup_id: str, answers: Dict[str, AnswerIn]) -> Report:
        """Create a repport"""
        report = ReportIn(standup_id=standup_id, answers=answers)
        response = await self._http_post(data=report.dict())
        return Report(**response.json())

    async def list(self):
        """gets reports and yields them as a generator"""
        response = await self._http_get()
        for report in response.json():
            yield Report(**report)


class _StandupClient(_AbstractClient):
    async def list(self):
        """gets Standups and yields them as a generator"""
        response = await self._http_get()
        print(response.json())
        for standup in response.json():
            yield Standup(**standup)

    async def get(self, standup_id: str) -> Standup:
        """gets a standup by id"""
        response = await self._http_get(path=standup_id)
        return Standup(**response.json())

    async def create(self) -> Standup:
        """Create a standup"""
        ...

    async def update(self, standup_id: str) -> Standup:
        """Update a standup"""
        ...

    async def duplicate(self, standup_id: str) -> Standup:
        """Duplicate a standup"""
        ...

    async def delete(self, standup_id: str) -> bool:
        """Delete a standup"""
        response = await self._http_delete(path=standup_id)
        return response.status_code == 200

    async def start(
        self,
        standup_id: str,
        user_ids: Optional[List[int]],
        emails: Optional[List[str]],
    ) -> bool:
        response = await self._http_post(
            path=f"{standup_id}/start", data={"users": user_ids, "emails": emails}
        )
        return response.status_code == 200


class GeekbotAPIClient:
    def __init__(self, config: GeekbotAPIConfig):
        self.config = config
        self.teams = _TeamClient(
            base_api_path=config.base_api_path,
            api_version=config.api_version,
            path="teams/",
            api_key=config.api_key,
        )
        self.reports = _ReportClient(
            base_api_path=config.base_api_path,
            api_version=config.api_version,
            path="reports/",
            api_key=config.api_key,
        )
        self.standups = _StandupClient(
            base_api_path=config.base_api_path,
            api_version=config.api_version,
            path="standups/",
            api_key=config.api_key,
        )
