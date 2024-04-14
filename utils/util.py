import os
import json
import time

def prepare_chacter_data(name=None):
    character_data = {
        "name": f"Character_test_{time.time()}",
        "universe": "Not exists",
        "education": "High school",
        "weight": 100,
        "height": 100,
        "identity": "Secret (known to the U.S. government)"
    }

    if name:
        character_data["name"] = name

    return character_data

def verify_dict_values(expected_dict_data: dict,
                       actual_dict_data: dict,
                       verified_fields: list = None,
                       unverified_fields: list = None):

    verified_keys = expected_dict_data.keys()
    if verified_fields:
        verified_keys = verified_fields
    elif unverified_fields:
        verified_keys -= unverified_fields
    for key in verified_keys:
        actual_value = actual_dict_data.get(key)
        expected_value = expected_dict_data.get(key)
        assert actual_value == expected_value
