#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from permutations import permute
from sure import that

class PermuteTestCase(TestCase):
    def test_empty_permute(self):
        results = permute([])
        assert results == []

    def test_trailing(self):
        results = permute([1,])
        assert results == [1]

    def test_permutations(self):
        results = permute([1,2])
        print results
        assert results == [[1,2],[2,1]]
