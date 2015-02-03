# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from generic_helpers import Section
from random import randrange as rr


# Definitions of set from http://en.wikipedia.org/wiki/Aleph_number


class Set(object):

    def __init__(self, items):
        self.items = set(items)

    def __setitem__(self, value):
        self.items.add(value)

    def __getitem__(self, value):
        return self.items[value]

    def __str__(self):
        return str(sorted(self.items))

    def add(self, item):
        self.__setitem__(item)

    def is_series(self):
        copy = list(self.items)
        for k, _ in enumerate(copy):
            try:
                if not self.is_successor(copy[k], copy[k + 1]):
                    yield False
            except IndexError:
                continue
        yield True

    def is_successor(self, prev, next):
        if prev >= next:
            return False
        return True

    def cardinality(self):
        return len(self.items)


class Aleph(Set):

    def __init__(self, cardinality):
        self._cardinality = cardinality
        self.items = set()
        super(Aleph, self).__init__(self.items)

    def run_until(self, maximum):
        print ('I am an aleph set of elements'
               ' with cardinality {}').format(
                   super(Aleph, self).cardinality())
        curr = 0
        for item in self:
            if curr >= maximum:
                break
            print 'continuum item:', item
            curr += 1


class AlephNull(Aleph):

    def __init__(self):
        self.items = []
        super(AlephNull, self).__init__(None)

    def __iter__(self):
        for item in self.items:
            yield item


class AllSquares(AlephNull):

    def __init__(self):
        self.start = 1
        super(AllSquares, self).__init__()

    def __iter__(self):
        while True:
            res = self.start * self.start
            self.start += 2
            yield res
        raise StopIteration


class AllOdds(AlephNull):

    def __init__(self):
        self.val = 1
        super(AllOdds, self).__init__()

    def __iter__(self):
        while True:
            self.val += 2
            yield self.val
        raise StopIteration


class AlephOne(Aleph):

    def __init__(self):
        super(AlephOne, self).__init__(1)


class AlephOmega(Aleph):

    def __init__(self):
        super(AlephOmega, self).__init__('omega')


class BethOne(Aleph):
    # For the curious...
    # http://en.wikipedia.org/wiki/Beth_number
    pass


with Section('Set theory'):
    set_series = Set([1, 2, 3, 4])
    print set_series
    print 'is series?', set_series.is_series().next()  # True
    print
    set_nonseries = Set([1, 22, 103, 4])
    for _ in range(50):
        set_nonseries.add(rr(1, 9999))
    print set_nonseries
    print
    print 'is series?', set_nonseries.is_series().next()  # False

with Section('Set theory - cardinality of the continuum examples'):
    all_squares = AllSquares()
    # Limit the count, without limiting the implementation of an 'infinite set'
    all_squares.run_until(10)

    all_odds = AllOdds()
    all_odds.run_until(10)