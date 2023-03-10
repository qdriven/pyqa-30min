#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Dict


## Python Class nad class type
class Foo:
    pass


x = Foo()
# <class '__main__.Foo'>
# <class '__main__.Foo'>
print(x.__class__)
print(type(x))
n = 5
d = {'x': 1, 'y': 2}
print(type(Foo))
print(type(Dict))
for obj in (n, d, x):
    print(obj.__class__)
    print(type(obj))
    print(type(obj) is obj.__class__)  ## all true

for t in int, float, dict, list, tuple:
    print(type(t))

# Type and Class, everything is object, and every object has a type
# x is an instance of class Foo. One type
# Foo is an instance of the type metaclass. Another Type
# type is also an instance of the type metaclass, so it is an instance of itself. Metaclass

## create in dynamic class

H1 = type("H1", (), {})
print(H1(), type(H1()))

H2 = type("H2", (H1,), {"attr": 100})
print(type(H2()), H2().attr)

H3 = type("H3", (H2,), {
    "attr": 100,
    "attr_val": lambda x: x.attr + 100
})

print(H3(), H3().attr_val())


def new(cls):
    x = object.__new__(cls)
    x.attr = 10
    return x


Foo.__new__ = new

f = Foo()
print(f.attr)


class Meta(type):
    def __new__(cls, name, bases, *args, **kwargs):
        x = super().__new__(cls, name, bases, kwargs)
        x.attr = 1000
        return x

    def __init__(cls, name, base, dct):
        cls.another_attr = "another_attr"

##  metaclasses can easily veer into the realm of being a “solution in search of a problem

class FooMeta(metaclass=Meta):
    pass


print(FooMeta().attr, FooMeta().another_attr)
