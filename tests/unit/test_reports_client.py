def test_get_reports_no_report(test_client):
    test_client["requests_mock"].get(
        url=test_client["client"].reports._get_request_path(), json=[])
    reports = list()
    for report in test_client["client"].reports.list():
        reports.append(report)

    assert len(reports) == 0


def test_get_reports_one_report(test_client, fake_report):
    test_client["requests_mock"].get(
        url=test_client["client"].reports._get_request_path(),
        json=fake_report.dict())
    reports = list()
    for report in test_client["client"].reports.list():
        reports.append(report)

    assert len(reports) == 1
    assert reports[0].standup_id == "standup-1"


def test_get_reports_many_reports(test_client, fake_report):
    test_client["requests_mock"].get(
        url=test_client["client"].reports._get_request_path(),
        json=[fake_report.dict(), fake_report.dict()])
    reports = list()
    for report in test_client["client"].reports.list():
        reports.append(report)

    assert len(reports) == 2
    assert reports[0].standup_id == "standup-1"
    assert reports[1].standup_id == "standup-1"
