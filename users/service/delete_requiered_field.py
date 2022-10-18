def delete_field(_dict: dict) -> dict:
    """
    Delete 'This field is required' error in form errors dict
    :param _dict:
    :return:
    """
    return {key: value for key, value in _dict.items()
            if value[0] != 'This field is required.'}
