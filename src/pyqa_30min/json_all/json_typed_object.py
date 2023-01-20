#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from pydantic import BaseModel

__all__ = [
    "Country",
    "class_to_dict",
    "class_to_json",
    "json_to_class",
    "dict_to_class"
]


class Country(BaseModel):
    name: str
    population: int
    languages: List[str]


c = Country(name="China", population=145565443, languages=["Chinese"])

json_str = """
{
   "name": "China",
   "population": 1431002651,
   "capital": "Beijing",
   "languages": [
      "Chinese"
   ]
}
"""

dict_demo = {
    "name": "United States",
    "population": 331002651,
    "capital": "Washington D.C.",
    "languages": [
        "English",
        "Spanish"
    ]
}


def class_to_json():
    return c.json()


def class_to_dict():
    return c.dict()


def dict_to_class():
    return Country.parse_obj(dict_demo)


def json_to_class():
    return Country.parse_raw(json_str)
