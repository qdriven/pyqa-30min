#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

dict_demo = {
    "name": "United States",
    "population": 331002651,
    "capital": "Washington D.C.",
    "languages": [
        "English",
        "Spanish"
    ]
}

__all__ = [
    "dict_to_json",
    "dict_to_json_file"
]


def dict_to_json():
    return json.dumps(dict_demo, ensure_ascii=True)


def dict_to_json_file(file_path: str):
    with open(file_path, 'w') as f:
        json.dump(file_path, f)
