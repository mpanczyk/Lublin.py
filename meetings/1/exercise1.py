#!/usr/bin/env python3


alist = [[['a'], 'a'], 'a', 'a', [[]]]

def flat_list(alist):
    #insert your code here
    pass


'''
# hint:
elem = []
isinstance( elem, list ) # -> true if elem is a list
# this above is (almost always) better than
type(elem) == list
'''

assert flat_list(alist) == ['a'] * 4
