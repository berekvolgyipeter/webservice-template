from unittest.mock import patch


@patch("app.routes.results.interactor.list_results", return_value={"status": "OK"})
def test_list_results(mock_list_results, mock_client):
    response = mock_client.get("/results?driver_name=Mika%20Hakkinen")
    assert response.json == {"status": "OK"}
    assert response.status_code == 200


@patch("app.routes.results.interactor.add_result", return_value={"status": "OK"})
def test_add_result(mock_list_results, mock_client):
    response = mock_client.post("/results", json={
        "driver_name": "Mika Hakkinen", "grand_prix": "1998 Australia", "position": 1})
    assert response.json == {"status": "OK"}
    assert response.status_code == 200
