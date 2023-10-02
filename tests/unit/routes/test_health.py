def test_health(mock_client):
    response = mock_client.get("/")
    assert response.json == {"status": "OK"}
    assert response.status_code == 200
