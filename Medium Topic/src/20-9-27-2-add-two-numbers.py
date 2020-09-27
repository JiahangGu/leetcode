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