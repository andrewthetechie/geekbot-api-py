import pytest


@pytest.mark.asyncio
async def test_async_get_reports_no_report(test_async_client):
    test_async_client["httpx_mock"].add_response(method="GET", json=[])
    reports = list()
    async for report in test_async_client["client"].async_reports.list():
        reports.append(report)

    assert len(reports) == 0


@pytest.mark.asyncio
async def test_async_get_reports_one_report(test_async_client, fake_report):
    test_async_client["httpx_mock"].add_response(method="GET",
                                                 json=fake_report.dict())
    reports = list()
    async for report in test_async_client["client"].async_reports.list():
        reports.append(report)

    assert len(reports) == 1
    assert reports[0].standup_id == "standup-1"


@pytest.mark.asyncio
async def test_async_get_reports_many_reports(test_async_client, fake_report):
    test_async_client["httpx_mock"].add_response(
        method="GET", json=[fake_report.dict(),
                            fake_report.dict()])
    reports = list()
    async for report in test_async_client["client"].async_reports.list():
        reports.append(report)

    assert len(reports) == 2
    assert reports[0].standup_id == "standup-1"
    assert reports[1].standup_id == "standup-1"
