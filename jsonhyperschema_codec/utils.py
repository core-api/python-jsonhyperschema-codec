from coreapi.compat import string_types


def _get_string(item, key):
    value = item.get(key)
    if isinstance(value, string_types):
        return value
    return ''


def _get_dict(item, key):
    value = item.get(key)
    if isinstance(value, dict):
        return value
    return {}


def _get_list(item, key):
    value = item.get(key)
    if isinstance(value, list):
        return value
    return []


def get_dicts(item):
    return [value for value in item if isinstance(value, dict)]


def _dereference(value, ref):
    keys = value.strip('#/').split('/')
    node = ref
    for key in keys:
        node = _get_dict(node, key)
    return node
