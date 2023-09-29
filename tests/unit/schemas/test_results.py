from pytest import mark
from schema import SchemaError

from app.schemas import results as results_schema


@mark.parametrize("params, exp_is_valid", [
    ({}, False),
    ({"driver_name": "Hakkinen"}, True),
    ({"driver_name": 123}, False),
    ({"place": 1}, True),
    ({"place": 0}, False),
    ({"grand_prix": "1998 Hungary"}, True),
    ({"grand_prix": 123}, False),
])
def test_results_schema(params, exp_is_valid):
    is_valid = True
    try:
        inp = results_schema.validate_optional_results_in(params)
        print(inp)
    except SchemaError as e:
        is_valid = False

    assert is_valid is exp_is_valid
