def obj_to_dict(obj):
    if isinstance(obj, dict):
        return {k: obj_to_dict(v) if isinstance(v,dict) else v for k, v in obj.items()}
    elif hasattr(obj, '__dict__'):
        return obj_to_dict(obj.__dict__)
    elif isinstance(obj, (list, tuple)):
        return [obj_to_dict(item) for item in obj]
    elif isinstance(obj, (int, float, str, bool, type(None))):
        return obj
    else:
        try:
            return obj.__dict__
        except AttributeError:
            return str(obj)
