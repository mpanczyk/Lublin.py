#!/usr/bin/env python3

import sys

# print module's name
# __name__ == '__main__' if run as a standalone script
# otherwise it is a name of the module
print(__name__)

def print_list(alist):
    for item in alist:
        print(item)

if __name__ == '__main__':
    print_list(sys.argv)
