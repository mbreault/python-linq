#!/usr/bin/env python

from py_linq import Enumerable

my_collection = Enumerable([1,2,3])
print(my_collection)

result =  Enumerable([
    {'value': 1},
    {'value': 2},
    {'value': 3}
]).single_or_default(lambda x: x['value'] == 3)
# {'value': 3}
print(result)

result = Enumerable([
    {'value': 1},
    {'value': 2},
    {'value': 3}
]).first_or_default()
print(result)
