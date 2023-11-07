def class_to_json(obj):
    """Returns the dictionary description for
    JSON serialization of an object"""
    data = {}

    for key, value in obj.__dict__.items():
        """Check if the attribute is a serializable data type"""
        if isinstance(value, (list, dict, str, int, bool)):
            data[key] = value
        else:
            """For non-serializable data types,
            store the attribute name and its type"""
            data[key] = str(type(value).__name__)

    return data
