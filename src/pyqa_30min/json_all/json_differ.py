#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pprint import pprint

from deepdiff import DeepDiff

t1 = {1:1, 2:2, 3:3}
t2 = {1:1, 2:"2", 3:3}

pprint(DeepDiff(t1, t2, verbose_level=0), indent=2)