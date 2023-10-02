from unittest.mock import patch


@patch("app.routes.results.schema.validate_optional_results_in", return_value={"param": "value"})
@patch("app.routes.results.interactor.list_results", return_value={"status": "OK"})
def test_list_results(mock_interactor, mock_schema, mock_client):
    params = {"driver_name": "Mika Hakkinen"}
    response = mock_client.get("/results", query_string=params)

    mock_schema.assert_called_once_with(params)
    mock_interactor.assert_called_once_with(mock_schema.return_value)
    assert response.json == {"status": "OK"}
    assert response.status_code == 200


@patch("app.routes.results.schema.validate_all_results_in", return_value={"param": "value"})
@patch("app.routes.results.interactor.add_result", return_value={"status": "OK"})
def test_add_result(mock_interactor, mock_schema, mock_client):
    params = {"driver_name": "Mika Hakkinen", "grand_prix": "1998 Australia", "position": 1}
    response = mock_client.post("/results", json=params)

    mock_schema.assert_called_once_with(params)
    mock_interactor.assert_called_once_with(mock_schema.return_value)
    assert response.json == {"status": "OK"}
    assert response.status_code == 200
