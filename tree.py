#!/usr/bin/env python
# -*- coding: utf-8 -*-

def max_depth(node):
    if node is None:
        return 0
    else:
        left_depth = max_depth(node.left)
        right_depth = max_depth(node.right)
        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1
