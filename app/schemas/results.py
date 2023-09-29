from schema import Schema, Optional, And, Use, SchemaError


class ResultsIn:
    def __init__(self, driver_name: str = None, grand_prix: str = None, position: int = None):
        self.driver_name = driver_name
        self.grand_prix = grand_prix
        self.position = position


OPTIONAL_RESULTS_IN = Schema(
    {
        Optional("driver_name"): str,
        Optional("grand_prix"): str,
        Optional("position"): And(Use(int), lambda x: x > 0),
    },
    ignore_extra_keys=True,
)

ALL_RESULTS_IN = Schema(
    {
        "driver_name": str,
        "grand_prix": str,
        "position": And(Use(int), lambda x: x > 0),
    },
    ignore_extra_keys=True,
)


def validate_optional_results_in(params: dict):
    params = OPTIONAL_RESULTS_IN.validate(params)
    if "driver_name" not in params and "grand_prix" not in params and "position" not in params:
        raise SchemaError("At least one of 'driver_name', 'grand_prix', or 'position' must be provided.")

    return ResultsIn(**params)


def validate_all_results_in(params: dict):
    params = ALL_RESULTS_IN.validate(params)
    return ResultsIn(**params)
