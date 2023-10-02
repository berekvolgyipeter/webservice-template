from pytest import mark
from schema import SchemaError

from app.schemas import drivers as schema


@mark.parametrize("params, exp_is_valid", [
    ({}, False),
    ({"name": "Hakkinen"}, True),
    ({"name": 123}, False),
    ({"team": "Mclaren Mercedes"}, True),
    ({"team": 123}, False),
    ({"name": "Hakkinen", "team": "Mclaren Mercedes"}, True),
])
def test_drivers_schema_optional(params, exp_is_valid):
    is_valid = True
    try:
        inp = schema.validate_optional_drivers_in(params)
        print(inp)
    except SchemaError as e:
        is_valid = False

    assert is_valid is exp_is_valid


@mark.parametrize("params, exp_is_valid", [
    ({}, False),
    ({"name": "Hakkinen"}, False),
    ({"team": "Mclaren Mercedes"}, False),
    ({"name": "Hakkinen", "team": "Mclaren Mercedes"}, True),
])
def test_drivers_schema_all(params, exp_is_valid):
    is_valid = True
    try:
        inp = schema.validate_all_drivers_in(params)
        print(inp)
    except SchemaError as e:
        is_valid = False

    assert is_valid is exp_is_valid
