def get_if_possible(element, json):
    """  returns the value of the dict key, according to its path """
    # if the key doesnt exists None will be returned.
    # i.e. get_if_possible("key1.key2", {"key1": {"key2": "abc"}} )
    try:
        keys = element.split('.')
        rv = json
        for key in keys:
            rv = rv[key]
        return rv

    except KeyError:
        return None
    except TypeError:
        return None
