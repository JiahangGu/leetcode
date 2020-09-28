#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/27 22:55
# @Author:JiahangGu
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        首先要操作首节点，建立一个tmp结点指向head，交换结点的方式如下
        假设pre指向当前要交换的结点对的前驱结点，则x=pre.next, y=pre.next.next
        pre.next = y
        x.next = y.next
        y.next = x
        具体代码不再实现，思路很清晰
        :param head:
        :return:
        """