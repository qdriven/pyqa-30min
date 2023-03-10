#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Any

import jinja2
from pydantic.main import BaseModel

tpl_env = jinja2.Environment()


def make_string_template(tpl_str: str) -> jinja2.Template:
    return tpl_env.from_string(tpl_str)


def render_str_template(tpl_str: str, context: Any) -> str:
    tpl = make_string_template(tpl_str)
    return tpl.render(context)


def hello_world():
    return "hello_world"


def greeting(name: str):
    return "Hello," + name;


class StructureClass(BaseModel):
    name: str = "name"
    value: str = "value"


def raw_render():
    tpl_str = """
    "Hello, {{ name.upper() }}!"
      Hello, {{ hello()}}!
      Hellom {{greet(name)}}
      Hellom {{ greet(name.upper()) }}
      Hello {{clazz.name}}
    """
    template = tpl_env.from_string(tpl_str)
    template.globals.update({
        "hello": hello_world,
        "greet": greeting
    })
    print(template.render(name="test",clazz=StructureClass()))


raw_render()
