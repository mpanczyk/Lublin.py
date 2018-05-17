#!/usr/bin/env python3


alist = [[['a'], 'a'], 'a', 'a', [[]]]

def flat_list(alist):
    if not isinstance(alist, list):
        return [alist]
    result = []
    for x in alist:
        result.extend(flat(x))
    return result


'''
# hint:
elem = []
isinstance( elem, list ) # -> true if elem is a list
# this above is (almost always) better than
type(elem) == list
'''

assert flat_list(alist) == ['a'] * 4
# ['a'] * 4 ==  ['a', 'a', 'a', 'a']
