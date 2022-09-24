def delete_field(_dict: dict) -> dict:
    return {key: value for key, value in _dict.items()
            if value[0] != 'This field is required.'}
