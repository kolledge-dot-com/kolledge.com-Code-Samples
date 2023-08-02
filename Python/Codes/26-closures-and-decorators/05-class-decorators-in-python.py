# Creating class decorators
def uppercase_class(cls):
    # Get all the class attributes
    attributes = cls.__dict__.copy()
    # Modify the attributes that are not under (special) methods
    for name, value in attributes.items():
        if not name.startswith("__") and callable(value):
            def uppercaser(*args, kwargs):
                result = value(*args, kwargs)
                if isinstance(result, str):
                    return result.upper()
                else:
                    return result

            setattr(cls, name, uppercaser)
    return cls
