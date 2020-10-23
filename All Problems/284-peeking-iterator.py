#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/23 16:15
# @Author:JiahangGu
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.p = []

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if len(self.p) > 0:
            return self.p[0]
        val = self.iter.next()
        self.p.append(val)
        return val

    def next(self):
        """
        :rtype: int
        """
        if len(self.p) > 0:
            val = self.p.pop(0)
            return val
        return self.iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iter.hasNext() or len(self.p) > 0

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
