from typing import List

included_method_names: List[str] | None = None
methods_to_export: List[str] | None = None
included_api_method_names: List[str] | None = None

def include_plot(func):
    global included_method_names
    if included_method_names:
        included_method_names.append(func.__name__)
    else:
        included_method_names = [func.__name__]
    return func

def export(func):
    global methods_to_export
    if methods_to_export:
        methods_to_export.append(func.__name__)
    else:
        methods_to_export = [func.__name__]
    return func


def include_to_api(func):
    global included_api_method_names
    if included_api_method_names:
        included_api_method_names.append(func.__name__)
    else:
        included_api_method_names = [func.__name__]
    return func
