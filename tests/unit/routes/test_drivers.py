from unittest.mock import patch


@patch("app.routes.drivers.schema.validate_optional_drivers_in", return_value={"param": "value"})
@patch("app.routes.drivers.interactor.list_drivers", return_value={"status": "OK"})
def test_list_drivers(mock_interactor, mock_schema, mock_client):
    params = {"name": "Mika Hakkinen"}
    response = mock_client.get("/drivers", query_string=params)

    mock_schema.assert_called_once_with(params)
    mock_interactor.assert_called_once_with(mock_schema.return_value)
    assert response.json == {"status": "OK"}
    assert response.status_code == 200


@patch("app.routes.drivers.schema.validate_all_drivers_in", return_value={"param": "value"})
@patch("app.routes.drivers.interactor.add_driver", return_value={"status": "OK"})
def test_add_driver(mock_interactor,  mock_schema, mock_client):
    params = {"name": "Mika Hakkinen", "team": "McLaren Mercedes"}
    response = mock_client.post("/drivers", json=params)

    mock_schema.assert_called_once_with(params)
    mock_interactor.assert_called_once_with(mock_schema.return_value)
    assert response.json == {"status": "OK"}
    assert response.status_code == 200
