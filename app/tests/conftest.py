import pytest


@pytest.fixture
def input_json():
    return {
        "balance": 10000.0,
        "limit": 10000.0,
        "operations": [
            {
                "type": "In",
                "spot": 1.0,
                "spread": 0.0,
                "fx_quantity": 5000.0,
                "created_at": "2023-07-19T21:07:22.556467"
            },
            {
                "type": "Out",
                "spot": 1.0, "spread": 0.0,
                "fx_quantity": 5000.0,
                "created_at": "2023-07-20T21:07:22.556467"
            }
        ]
    }
