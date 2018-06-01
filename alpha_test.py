#! /usr/bin/env python3
# coding: utf-8
import unittest
from alpha import Alpha
from reader import read
import os

class TestAlpha(unittest.TestCase):

    model0 = Alpha(read(os.path.join("test", "test0.txt")))
    model1 = Alpha(read(os.path.join("test", "test1.txt")))
    model2 = Alpha(read(os.path.join("test", "test2.txt")))

    def __equality_check(self, s0, s1, s2, set_name):
        temp = [[TestAlpha.model0, s0], [TestAlpha.model1, s1], [TestAlpha.model2, s2]]
        for model, s in temp:
            val = getattr(model, set_name)
            self.assertEqual(val, s)
    
    def __order_independent_equality_check(self, s0, s1, s2, set_name):
        s0_new, s1_new, s2_new = [], [], []
        for s in zip([s0_new, s1_new, s2_new], [s0, s1, s2]):
            any(s[0].append((set(i[0]), set(i[1]))) for i in s[1])

        temp = [[TestAlpha.model0, s0_new], [TestAlpha.model1, s1_new], [TestAlpha.model2, s2_new]]
        for model, s in temp:
            val = getattr(model, set_name)
            val_new = []
            any(val_new.append((set(i[0]), set(i[1]))) for i in val)
            def eq(p, q):
                a, b = p[:], q[:]
                if len(a) != len(b):
                    return False
                while a:
                    temp = a.pop()
                    if temp not in b:
                        return False
                return True
            self.assertTrue(eq(val_new, s))

    def test_tl_set(self):
        s0 = {'a', 'b', 'c', 'd', 'e', 'f'}
        s1 = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
        s2 = {'a', 'b', 'c', 'd', 'e', 'f'}
        self.__equality_check(s0, s1, s2, 'tl')

    def test_ti_set(self):
        s0 = {'a'}
        s1 = {'a'}
        s2 = {'a', 'b', 'd'}
        self.__equality_check(s0, s1, s2, 'ti')

    def test_to_set(self):
        s0 = {'f'}
        s1 = {'d'}
        s2 = {'f'}
        self.__equality_check(s0, s1, s2, 'to')
    
    def test_xl_set(self):
        s0 = {(('a',), ('b',)), (('a',), ('e',)), (('a', 'd'), ('b',)), (('b',), ('c',)), (('b',), ('f',)), 
              (('b',), ('f', 'c')), (('c',), ('d',)), (('d',), ('b',)), (('e',), ('f',))}
        s1 = {(('a',), ('b',)), (('a',), ('b', 'e')), (('a',), ('c',)), (('a',), ('c', 'e')), (('a',), ('e',)), 
              (('b',), ('d',)), (('b', 'g'), ('d',)), (('b', 'g', 'h'), ('d',)), (('b', 'h'), ('d',)), (('c',), ('d',)), 
              (('c', 'f'), ('d',)), (('c', 'f', 'g'), ('d',)), (('c', 'f', 'g', 'h'), ('d',)), (('c', 'f', 'h'), ('d',)), 
              (('c', 'g'), ('d',)), (('c', 'g', 'h'), ('d',)), (('c', 'h'), ('d',)), (('e',), ('f',)), (('e',), ('f', 'g')), 
              (('e',), ('f', 'g', 'h')), (('e',), ('f', 'h')), (('e',), ('g',)), (('e',), ('g', 'h')), (('e',), ('h',)), 
              (('f',), ('d',)), (('f', 'b'), ('d',)), (('f', 'b', 'g'), ('d',)), (('f', 'b', 'g', 'h'), ('d',)), 
              (('f', 'b', 'h'), ('d',)), (('f', 'g'), ('d',)), (('f', 'g', 'h'), ('d',)), (('f', 'h'), ('d',)), (('g',), ('d',)), 
              (('g', 'h'), ('d',)), (('h',), ('d',))}
        s2 = {(('a',), ('b',)), (('a',), ('c',)), (('a',), ('e',)), (('b',), ('e',)), (('c',), ('e',)), (('c',), ('f',)), 
              (('d',), ('a',)), (('d',), ('e',)), (('e',), ('f',))}
        self.__order_independent_equality_check(s0, s1, s2, 'xl')
    
    def test_yl_set(self):
        s0 = {(('a',), ('e',)), (('a', 'd'), ('b',)), (('b',), ('f', 'c')), (('c',), ('d',)), (('e',), ('f',))}
        s1 = {(('a',), ('b', 'e')), (('a',), ('c', 'e')), (('c', 'f', 'g', 'h'), ('d',)), (('e',), ('f', 'g', 'h')), 
              (('f', 'b', 'g', 'h'), ('d',))}
        s2 = {(('a',), ('b',)), (('a',), ('c',)), (('a',), ('e',)), (('b',), ('e',)), (('c',), ('e',)), (('c',), ('f',)), 
              (('d',), ('a',)), (('d',), ('e',)), (('e',), ('f',))}
        self.__order_independent_equality_check(s0, s1, s2, 'yl')
    
    def test_ds_set(self):
        s0 = {('a', 'b'), ('a', 'e'), ('b', 'c'), ('b', 'e'), ('b', 'f'), ('c', 'd'), ('c', 'e'), ('d', 'b'), 
              ('d', 'e'), ('e', 'b'), ('e', 'c'), ('e', 'd'), ('e', 'f')}
        s1 = {('a', 'b'), ('a', 'c'), ('a', 'e'), ('b', 'c'), ('b', 'd'), ('c', 'b'), ('c', 'd'), ('e', 'f'), 
              ('e', 'g'), ('e', 'h'), ('f', 'd'), ('g', 'd'), ('h', 'd')}
        s2 = {('a', 'b'), ('a', 'c'), ('a', 'e'), ('b', 'b'), ('b', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'b'), 
              ('c', 'd'), ('c', 'e'), ('c', 'f'), ('d', 'a'), ('d', 'b'), ('d', 'c'), ('d', 'e'), ('e', 'f')}
        self.__equality_check(s0, s1, s2, 'ds')
    
    def test_cs_set(self):
        s0 = {('a', 'b'), ('a', 'e'), ('b', 'c'), ('b', 'f'), ('c', 'd'), ('d', 'b'), ('e', 'f')}
        s1 = {('a', 'b'), ('a', 'c'), ('a', 'e'), ('b', 'd'), ('c', 'd'), ('e', 'f'), ('e', 'g'), ('e', 'h'), 
              ('f', 'd'), ('g', 'd'), ('h', 'd')}
        s2 = {('a', 'b'), ('a', 'c'), ('a', 'e'), ('b', 'e'), ('c', 'e'), ('c', 'f'), ('d', 'a'), ('d', 'e'), 
              ('e', 'f')}
        self.__equality_check(s0, s1, s2, 'cs')
    
    def test_pr_set(self):
        s0 = {('b', 'e'), ('c', 'e'), ('d', 'e'), ('e', 'b'), ('e', 'c'), ('e', 'd')}
        s1 = {('b', 'c'), ('c', 'b')}
        s2 = {('b', 'b'), ('b', 'c'), ('b', 'd'), ('c', 'b'), ('c', 'd'), ('d', 'b'), ('d', 'c')}
        self.__equality_check(s0, s1, s2, 'pr')
    
    def test_ind_set(self):
        s0 = {('a', 'c'), ('a', 'd'), ('a', 'f'), ('c', 'a'), ('c', 'f'), ('d', 'a'), ('d', 'f'), ('f', 'a'), 
              ('f', 'c'), ('f', 'd')}
        s1 = {('a', 'd'), ('a', 'f'), ('a', 'g'), ('a', 'h'), ('b', 'e'), ('b', 'f'), ('b', 'g'), ('b', 'h'), 
              ('c', 'e'), ('c', 'f'), ('c', 'g'), ('c', 'h'), ('d', 'a'), ('d', 'e'), ('e', 'b'), ('e', 'c'), ('e', 'd'), 
              ('f', 'a'), ('f', 'b'), ('f', 'c'), ('f', 'g'), ('f', 'h'), ('g', 'a'), ('g', 'b'), ('g', 'c'), ('g', 'f'), 
              ('g', 'h'), ('h', 'a'), ('h', 'b'), ('h', 'c'), ('h', 'f'), ('h', 'g')}
        s2 = {('a', 'f'), ('b', 'f'), ('d', 'f'), ('f', 'a'), ('f', 'b'), ('f', 'd')}
        self.__equality_check(s0, s1, s2, 'ind')
