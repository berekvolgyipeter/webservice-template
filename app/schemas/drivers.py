from schema import Schema, Optional, SchemaError


class DriversIn:
    def __init__(self, name: str = None, team: str = None):
        self.name = name
        self.team = team


OPTIONAL_DRIVERS_IN = Schema(
    {
        Optional("name"): str,
        Optional("team"): str,
    },
    ignore_extra_keys=True,
)

ALL_DRIVERS_IN = Schema(
    {
        "name": str,
        "team": str,
    },
    ignore_extra_keys=True,
)


def validate_optional_drivers_in(params: dict):
    params = OPTIONAL_DRIVERS_IN.validate(params)
    if "name" not in params and "team" not in params:
        raise SchemaError("At least one of 'name' or 'team' must be provided.")

    return DriversIn(**params)


def validate_all_drivers_in(params: dict):
    params = ALL_DRIVERS_IN.validate(params)
    return DriversIn(**params)
