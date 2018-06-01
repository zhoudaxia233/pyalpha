#! /usr/bin/env python3
# coding: utf-8
import unittest
from alpha import Alpha
from reader import read
import os

class TestAlpha(unittest.TestCase):
    def test_init(self):
        file_for_testing = os.path.join("test", "test0.txt")
        log = read(file_for_testing)
        alpha_model = Alpha(log)
        s = {'f', 'b', 'd', 'a', 'e', 'c'}
        self.assertEqual(alpha_model.tl, s)
