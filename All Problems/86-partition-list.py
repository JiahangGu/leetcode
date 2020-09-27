#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/24 20:51
# @Author:JiahangGu
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        新建链表，两次遍历，一次小于x，一次大于等于x。
        :param head:
        :param x:
        :return:
        """
        # tmp = head
        # root = ListNode(0)
        # pre = root
        # while tmp:
        #     if tmp.val < x:
        #         pre.next = ListNode(tmp.val)
        #         pre = pre.next
        #     tmp = tmp.next
        # tmp = head
        # while tmp:
        #     if tmp.val >= x:
        #         pre.next = ListNode(tmp.val)
        #         pre = pre.next
        #     tmp = tmp.next
        # return root.next
        """
        一种优化的方式，可以使用双指针，一个指向小于x的链表，一个指向大于等于x，最后拼接起来。
        """
        small = ListNode(0)
        big = ListNode(0)
        s = small
        b = big
        while head:
            if head.val < x:
                s.next = ListNode(head.val)
                s = s.next
            else:
                b.next = ListNode(head.val)
                b = b.next
            head = head.next
        s.next = b.next
        return small.next