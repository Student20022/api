from tests.conftest import client


def test_index_redirect(client) -> None:
    response = client.get('/')
    assert response.status_code == 302 
    assert '/report' in response.location


def test_report_page_asc_order(client) -> None:
    response = client.get('/report?order=asc')
    assert response.status_code == 200
    assert 'text/plain; charset=utf-8' in response.content_type
    assert 'Position' in response.get_data(as_text=True)
    assert len(response.get_data(as_text=True).split('\n')) == 20


def test_report_page_desc_order(client) -> None:
    response = client.get('/report?order=desc')
    assert response.status_code == 200
    assert 'text/plain; charset=utf-8' in response.content_type
    assert 'Position' in response.get_data(as_text=True)
    assert len(response.get_data(as_text=True).split('\n')) == 20


def test_driver_list_asc(client) -> None:
    response = client.get('/report/drivers/?order=asc')
    html_content = response.data.decode('utf-8')
    assert response.status_code == 200
    assert 'text/html' in response.content_type
    assert 'Abbreviation' in html_content
    assert html_content.count('<tr>') == 20


def test_driver_list_desc(client) -> None:
    response = client.get('/report/drivers/?order=desc')
    html_content = response.data.decode('utf-8')
    assert response.status_code == 200
    assert 'text/html' in response.content_type
    assert 'Abbreviation' in html_content
    assert html_content.count('<tr>') == 20


def test_about_driver(client) -> None:
    response = client.get('/report/drivers?driver_id=KRF')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert all("Position" in entry for entry in data)