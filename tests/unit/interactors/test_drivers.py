from schemas.drivers import DriversIn
import app.interactors.drivers as interactor


def test_drivers(mock_session):
    result = interactor.list_drivers(DriversIn(team="Mclaren Mercedes"))
    assert result == {"status": "OK", "drivers": []}

    interactor.add_driver(DriversIn(name="Mika Hakkinen", team="McLaren Mercedes"))
    interactor.add_driver(DriversIn(name="David Coulthard", team="McLaren Mercedes"))

    result = interactor.list_drivers(DriversIn())
    assert result == {
        "status": "OK",
        "drivers": [
            {"name": "Mika Hakkinen", "team": "McLaren Mercedes"},
            {"name": "David Coulthard", "team": "McLaren Mercedes"},
        ]
    }
