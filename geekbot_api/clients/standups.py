from typing import List
from typing import Optional

from . import _AbstractClient
from ..schemas import Standup
from ..schemas import StandupDuplicateIn
from ..schemas import StandupIn


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

    async def create(self, standup_in: StandupIn) -> Standup:
        """Create a standup"""
        response = await self._http_post(data=standup_in.dict())
        return Standup(**response.json())

    async def update(self, standup_id: str, standup_in: StandupDuplicateIn) -> Standup:
        """Update a standup"""
        response = await self._http_patch(data=standup_id.dict())
        return Standup(**response.json())

    async def duplicate(
        self, standup_id: str, standup_in: StandupDuplicateIn
    ) -> Standup:
        """Duplicate a standup"""
        response = await self._http_post(
            path=f"{standup_id}/duplicate", data=standup_in.dict()
        )
        return Standup(**response.json())

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
