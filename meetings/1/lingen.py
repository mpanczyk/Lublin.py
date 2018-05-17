#!/usr/bin/env python

import random

def as_list(fun):
    def f(*args, **kwargs):
        return list(fun(*args, **kwargs))
    return f

@as_list
def even_list(size=20, separator='#', elem='elem'):
    for _ in range(size-1):
        yield elem
        yield separator
    yield elem

def random_list(size):
    if random.randint(0, 1) == 1:
        return 'a'
    if size == 0:
        return []
    size = random.randint(1, size)
    return [random_list(size-1) for _ in range(size)]
