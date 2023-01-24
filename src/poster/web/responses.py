#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Optional

from pydantic import BaseModel

__all__=[
    "ok",
    "PosterResponse",
    "error",
    "expired"
]
class PosterResponse(BaseModel):
    code: int = 0
    msg: Optional[str] = "successful"

    def __str__(self):
        return self.json()

    def __repr__(self):
        return self.json()


def ok() -> PosterResponse:
    return PosterResponse()


def error(msg='failure'):
    return PosterResponse(code=400, msg=msg)


def expired(msg="token expired") -> PosterResponse:
    return PosterResponse(code=401, msg=msg)
