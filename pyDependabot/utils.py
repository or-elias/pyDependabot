from pydependabot.consts import NOT_POPULATED

class Logger(object):
    def __init__(self, print_debug_log):
        self.print_debug_log = print_debug_log

    def debug(self, line):
        if self.print_debug_log:
            print(f"[DEBUG] {line}")
    

def get_if_possible(json, element):
    """  returns the value of the dict key, according to its path """
    # if the key doesnt exists NOT_POPULATED will be returned.
    # i.e. get_if_possible("key1.key2", {"key1": {"key2": "abc"}} )
    try:
        keys = element.split('.')
        rv = json
        for key in keys:
            rv = rv[key]
        return rv

    except KeyError:
        return NOT_POPULATED
    except TypeError:
        return NOT_POPULATED

