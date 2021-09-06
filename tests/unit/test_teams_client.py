def test_get_teams_no_team(test_client):
    test_client["requests_mock"].get(
        url=test_client["client"].teams._get_request_path(), json=[]
    )
    teams = list()
    for team in test_client["client"].teams.list():
        teams.append(team)

    assert len(teams) == 0


def test_get_teams_one_team(test_client, fake_team):
    test_client["requests_mock"].get(
        url=test_client["client"].teams._get_request_path(), json=fake_team.dict()
    )
    teams = list()
    for team in test_client["client"].teams.list():
        teams.append(team)

    assert len(teams) == 1
    assert teams[0].name == fake_team.name


def test_get_teams_many_teams(test_client, fake_team):
    test_client["requests_mock"].get(
        url=test_client["client"].teams._get_request_path(),
        json=[fake_team.dict(), fake_team.dict()],
    )
    teams = list()
    for team in test_client["client"].teams.list():
        teams.append(team)

    assert len(teams) == 2
    assert teams[0].name == fake_team.name
    assert teams[1].name == fake_team.name
