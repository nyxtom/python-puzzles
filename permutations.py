#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

def permute(values):
    if len(values) <= 1:
        yield str
    else:
        for perm in permute(values[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + values[0:1] + perm[i:]
