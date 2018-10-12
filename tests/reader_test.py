#! /usr/bin/env python3
# coding: utf-8
import unittest
from pyalpha.reader import read
import os

class TestReader(unittest.TestCase):
    def test_read_test0(self):
        file_for_testing = os.path.join("tests", "test0.txt")
        log = read(file_for_testing)
        s = [('a', 'b', 'e', 'f'), ('a', 'b', 'e', 'c', 'd', 'b', 'f'), 
        ('a', 'b', 'c', 'e', 'd', 'b', 'f'), ('a', 'b', 'c', 'd', 'e', 'b', 'f'), 
        ('a', 'e', 'b', 'c', 'd', 'b', 'f')]
        self.assertListEqual(log, s)
    
    def test_read_test1(self):
        file_for_testing = os.path.join("tests", "test1.txt")
        log = read(file_for_testing)
        s = [('a', 'b', 'c', 'd'), ('a', 'c', 'b', 'd'), ('a', 'e', 'f', 'd'), ('a', 'e', 'g', 'd'), ('a', 'e', 'h', 'd')]
        self.assertListEqual(log, s)

    def test_read_test2(self):
        file_for_testing = os.path.join("tests", "test2.txt")
        log = read(file_for_testing)
        s = [('d', 'c', 'b', 'e', 'f'), ('a', 'e', 'f'), ('d', 'b', 'b', 'c', 'e', 'f'), ('a', 'b', 'c', 'd', 'e', 'f'), 
        ('b', 'd', 'a', 'c', 'f')]
        self.assertListEqual(log, s)

