#!/usr/bin/env python

import string

list1 = [
    'a', '1', 1, ['a'], 'Ala ma kota', 3.14159,
    string.ascii_letters,
    string.punctuation,
    string.printable,
]


'''
# Make a new list, which consists of the values from `list1`
# converted to strings.
# Use list comprehension.

list2 = ...

assert [
    'a',
    '1',
    '1',
    "['a']",
    'Ala ma kota',
    '3.14159',
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~',
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c',
] == list2
#'''




'''
# The same as above, but take only non-string values from original list.
# Use list comprehension.

list3 = ...

assert ['1', "['a']", '3.14159'] == list3
#'''

