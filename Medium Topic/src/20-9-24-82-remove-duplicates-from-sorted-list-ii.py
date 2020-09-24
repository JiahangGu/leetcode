#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/24 18:03
# @Author:JiahangGu
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        给定的是有序链表，则只需向后查找到第一个不相等的值，这中间的都要删掉。所以需要记录该节点的前驱节点。
        这里使用一个新建节点方便返回最终节点。
        :param head:
        :return:
        """
        if not head:
            return None
        root = ListNode(0)
        root.next = head
        pre = root
        while head:
            tmp = head
            while tmp and tmp.val == head.val:
                tmp = tmp.next
            # 需要判断如下情况， 1.tmp为None，此时分删除和不删除两种情况，删除则直接把前驱next置空；
            # 2.tmp不None，此时需要分删除和不删除，删除则把前驱的next置为tmp
            if not tmp:
                if head.next != tmp:
                    pre.next = None
                break
            else:
                if head.next == tmp:
                    pre = head
                    head = tmp
                else:
                    pre.next = tmp
                    head = tmp
        return root.next