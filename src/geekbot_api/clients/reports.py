from . import _AbstractAsyncClient
from . import _AbstractClient
from ..schemas import Report
from ..schemas import ReportIn


class _ReportsClient(_AbstractClient):

    def create(self, report: ReportIn) -> Report:
        """Create a repport"""
        response = self._http_post(data=report.dict())
        return Report(**response.json())

    def list(self):
        """gets reports and yields them as a generator"""
        response = self._http_get()
        response_json = response.json()
        if isinstance(response_json, list):
            if len(response_json) == 0:
                return
            else:
                for report in response.json():
                    yield Report(**report)
        else:
            yield Report(**response_json)


class _ReportsAsyncClient(_AbstractAsyncClient):

    async def create(self, report: ReportIn) -> Report:
        """Create a repport"""
        response = await self._http_post(data=report.dict())
        return Report(**response.json())

    async def list(self):
        """gets reports and yields them as a generator"""
        response = await self._http_get()
        response_json = response.json()
        if isinstance(response_json, list):
            if len(response_json) == 0:
                return
            else:
                for report in response_json:
                    yield Report(**report)
        else:
            yield Report(**response_json)
