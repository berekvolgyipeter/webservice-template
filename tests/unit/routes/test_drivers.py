from unittest.mock import patch


@patch("app.routes.drivers.interactor.list_drivers", return_value={"status": "OK"})
def test_list_drivers(mock_list_drivers, mock_client):
    response = mock_client.get("/drivers?name=Mika%20Hakkinen")
    assert response.json == {"status": "OK"}
    assert response.status_code == 200


@patch("app.routes.drivers.interactor.add_driver", return_value={"status": "OK"})
def test_add_driver(mock_list_drivers, mock_client):
    response = mock_client.post("/drivers", json={"name": "Mika Hakkinen", "team": "McLaren Mercedes"})
    assert response.json == {"status": "OK"}
    assert response.status_code == 200
