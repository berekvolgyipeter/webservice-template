from pytest import mark
from schema import SchemaError

from app.schemas import results as schema


@mark.parametrize("params, exp_is_valid", [
    ({}, False),
    ({"driver_name": "Hakkinen"}, True),
    ({"driver_name": 123}, False),
    ({"position": 1}, True),
    ({"position": 0}, False),
    ({"grand_prix": "1998 Hungary"}, True),
    ({"grand_prix": 123}, False),
])
def test_results_schema_optional(params, exp_is_valid):
    is_valid = True
    try:
        inp = schema.validate_optional_results_in(params)
        print(inp)
    except SchemaError as e:
        is_valid = False

    assert is_valid is exp_is_valid


@mark.parametrize("params, exp_is_valid", [
    ({}, False),
    ({"driver_name": "Hakkinen"}, False),
    ({"position": 1}, False),
    ({"grand_prix": "1998 Hungary"}, False),
    ({"driver_name": "Hakkinen", "position": 1}, False),
    ({"driver_name": "Hakkinen", "position": 1, "grand_prix": "1998 Hungary"}, True),
])
def test_results_schema_all(params, exp_is_valid):
    is_valid = True
    try:
        inp = schema.validate_all_results_in(params)
        print(inp)
    except SchemaError as e:
        is_valid = False

    assert is_valid is exp_is_valid
