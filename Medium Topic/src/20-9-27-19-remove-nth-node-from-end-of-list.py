#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/27 22:05
# @Author:JiahangGu
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        移除倒数第n个结点，很容易想到使用快慢指针的解法，快慢指针相差n-1个结点，在快指针到末尾的时候，
        满指针刚好到倒数第n个结点的前驱，移除第n个结点即可。
        注意，所有对链表进行操作的情况中，如果原始链表首节点有可能被删除，那么要在前面添加一个结点指向
        首节点，作为代理首节点方便处理
        :param head:
        :param n:
        :return:
        """
        root = ListNode(0)
        root.next = head
        fast = root
        slow = root
        while fast and n:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return root.next
