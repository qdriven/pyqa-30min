#!/usr/bin/env python
# -*- coding:utf-8 -*-

__all__ = [
    "method_1",
    "method_2",
    "all_templates"
]

from typing import List

all_templates = """
    __all__ = [
      %s
    ]
"""


def method_1():
    print("method_1")


def method_2():
    print("method_2")


def all_templates(methods: List) -> str:
    return ",".join(["%s".format(method) for method in methods])


if __name__ == '__main__':
    print(dir())
