#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
__all__=[
    "encode_json",
    "decode_json"
]
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


class Country:
    def __init__(self, name, population, languages):
        self.name = name
        self.population = population
        self.languages = languages


class CountryEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Country):
            # JSON object would be a dictionary.
            return {
                "name": o.name,
                "population": o.population,
                "languages": o.languages
            }
        else:
            # Base class will raise the TypeError.
            return super().default(o)


class CountryDecoder(json.JSONDecoder):
    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, o):
        decoded_country = Country(
            o.get('name'),
            o.get('population'),
            o.get('languages'),
        )
        return decoded_country


canada = Country("Canada", 37742154, ["English", "French"])

print(json.dumps(canada, cls=CountryEncoder))


# OUTPUT:   TypeError: Object of type Country is not JSON serializable

def decode_json():
    return json.loads(json_str, cls=CountryDecoder)


def encode_json():
    return json.dumps(canada, cls=CountryEncoder)
