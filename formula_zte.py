import re
from os.path import dirname, basename, isfile, join
import glob
from kpi.zte import *
modules = glob.glob(join(dirname(__file__), 'kpi', 'zte', "*.py"))


def default_func(a, b):
    return None


def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


list_formula = [basename(f)[:-3] for f in modules if isfile(f)
                and not f.endswith('__init__.py')]

formulas = {x: getattr(globals()[x], camel_to_snake(
    x), default_func) for x in list_formula}

# for x in sorted(formulas.items(), key=lambda x: x[0]):
#     print(f"{x[0].ljust(20)} : {x[1]}")
