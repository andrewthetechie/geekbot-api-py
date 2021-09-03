from typing import Dict

from . import _AbstractClient
from ..schemas import AnswerIn
from ..schemas import Report
from ..schemas import ReportIn


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
