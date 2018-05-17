#!/usr/bin/env python3

import lingen # my custom module in the same directory

alist = lingen.even_list(size=5)
print(alist)

# FYI: the value of `alist`:
assert alist == ['elem', '#', 'elem', '#', 'elem', '#', 'elem', '#', 'elem']


'''
# replace dots with your code
assert ... == ['elem', 'elem', 'elem', 'elem', 'elem']

#'''

new_list = filter(lambda item: item != '#', alist)
print(list(new_list))
