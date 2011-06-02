#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
def shuffle(items):
    size = len(items)
    for i in range(size):
        index = random.randint(i, size)
        items[i], items[index] = items[i], items[index]
