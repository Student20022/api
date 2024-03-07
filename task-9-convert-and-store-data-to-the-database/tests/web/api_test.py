from tests.conftest import client


def test_report_resource_json(client) -> None:
    response = client.get('/api/v1/report/?format=json')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 19
    assert all("Position" in entry for entry in data)


def test_report_resource_xml(client) -> None:
    response = client.get('/api/v1/report/?format=xml')
    assert response.status_code == 200
    data = response.get_data(as_text=True)
    assert '<report>' in data
    assert '<Position>' in data


def test_driver_resource_json(client) -> None:
    response = client.get('/api/v1/report/drivers/?format=json')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 19
    assert all("Abbreviation" in entry for entry in data)


def test_driver_resource_xml(client) -> None:
    response = client.get('/api/v1/report/drivers/?format=xml')
    assert response.status_code == 200
    data = response.get_data(as_text=True)
    assert '<report>' in data
    assert '<Abbreviation>' in data


def test_about_resource_json(client) -> None:
    response = client.get('/api/v1/report/drivers/about/?driver_id=KRF&format=json')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert all("Position" in entry for entry in data)


def test_about_resource_xml(client):
    response = client.get('/api/v1/report/drivers/about/?driver_id=KRF&format=xml')
    data = response.get_data(as_text=True)
    assert response.status_code == 200
    assert '<report>' in data
    assert '<Position>' in data
