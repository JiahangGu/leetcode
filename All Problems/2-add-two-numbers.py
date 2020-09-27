#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/27 10:26
# @Author:JiahangGu
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        类似于大数加法，在两个链表都没有到达尾部的时候，记录一个进位，加到下一个结点的和。如果有个链表遍历完成，
        则返回。
        :param l1:
        :param l2:
        :return:
        """
        c = 0
        t1 = l1
        pre1 = None
        pre2 = None
        while l1 and l2:
            val = l1.val + l2.val + c
            c = val // 10
            l1.val = val % 10
            pre1 = l1
            l1 = l1.next
            l2 = l2.next
        if l2:
            pre1.next = l2
            l1 = l2
        while l1:
            val = l1.val + c
            c = val // 10
            l1.val = val % 10
            pre1 = l1
            l1 = l1.next
        if c:
            pre1.next = ListNode(c)
        return t1
