import pytest


@pytest.mark.asyncio
async def test_async_list_standups_no_standup(test_async_client):
    test_async_client["httpx_mock"].add_response(method="GET", json=[])
    standups = list()
    async for team in test_async_client["client"].async_standups.list():
        standups.append(team)

    assert len(standups) == 0


@pytest.mark.asyncio
async def test_async_list_standups_one_team(test_async_client, fake_standup):
    test_async_client["httpx_mock"].add_response(method="GET", json=fake_standup.dict())
    standups = list()
    async for standup in test_async_client["client"].async_standups.list():
        standups.append(standup)

    assert len(standups) == 1
    assert standups[0].name == fake_standup.name


@pytest.mark.asyncio
async def test_async_list_standups_many_standups(test_async_client, fake_standup):
    test_async_client["httpx_mock"].add_response(
        method="GET", json=[fake_standup.dict(), fake_standup.dict()]
    )
    standups = list()
    async for standup in test_async_client["client"].async_standups.list():
        standups.append(standup)

    assert len(standups) == 2
    assert standups[0].name == fake_standup.name
    assert standups[1].name == fake_standup.name


@pytest.mark.asyncio
async def test_async_get_standup_no_standup(test_async_client):
    test_async_client["httpx_mock"].add_response(method="GET", status_code=404)

    standup = await test_async_client["client"].async_standups.get("1234")
    assert standup is None


@pytest.mark.asyncio
async def test_async_get_standup(test_async_client, fake_standup):
    test_async_client["httpx_mock"].add_response(method="GET", json=fake_standup.dict())

    standup = await test_async_client["client"].async_standups.get("1234")
    assert standup == fake_standup
