#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/8 10:38
# @Author:JiahangGu
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """

        :param head:
        :return:
        """

d = dict()
node = ListNode(1)
d[1] = node
print(d[1])
del d[1]
print(d.get(1, None))
print(node)