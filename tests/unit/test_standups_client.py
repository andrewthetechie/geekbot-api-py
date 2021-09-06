def test_list_standups_no_team(test_client):
    test_client["requests_mock"].get(
        url=test_client["client"].standups._get_request_path(), json=[]
    )
    standups = list()
    for team in test_client["client"].standups.list():
        standups.append(team)

    assert len(standups) == 0


def test_list_standups_one_team(test_client, fake_standup):
    test_client["requests_mock"].get(
        url=test_client["client"].standups._get_request_path(), json=fake_standup.dict()
    )
    standups = list()
    for standup in test_client["client"].standups.list():
        standups.append(standup)

    assert len(standups) == 1
    assert standups[0].name == fake_standup.name


def test_list_standups_many_standups(test_client, fake_standup):
    test_client["requests_mock"].get(
        url=test_client["client"].standups._get_request_path(),
        json=[fake_standup.dict(), fake_standup.dict()],
    )
    standups = list()
    for standup in test_client["client"].standups.list():
        standups.append(standup)

    assert len(standups) == 2
    assert standups[0].name == fake_standup.name
    assert standups[1].name == fake_standup.name


def test_get_standup_no_standup(test_client):
    test_client["requests_mock"].get(
        url=f"{test_client['client'].standups._get_request_path()}/1234",
        status_code=404,
    )

    standup = test_client["client"].standups.get("1234")
    assert standup is None


def test_get_standup(test_client, fake_standup):
    test_client["requests_mock"].get(
        url=f"{test_client['client'].standups._get_request_path()}/1234",
        json=fake_standup.dict(),
    )

    standup = test_client["client"].standups.get("1234")
    assert standup == fake_standup
