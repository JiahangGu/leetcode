#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/24 21:03
# @Author:JiahangGu
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        首先计算链表长度n，则实际移动k%n步。然后建立tail指向head的指针形成环，模拟移动即可。
        注意在返回之前将前一个节点的next置为null。
        注意要返回旋转k次的，也就是从末尾向前移动k-1次的节点为首节点，那么从首节点出发的移动个数为n-k-1，这里是因为
        二者起点不同，一个是首，一个是尾。并且是记录到head.next所以要-1.
        :param head:
        :param k:
        :return:
        """
        # if not head:
        #     return None
        # length = 1
        # tmp = head
        # while head.next:
        #     length += 1
        #     head = head.next
        # steps = length - k % length - 1
        # head.next = tmp
        # while steps:
        #     tmp = tmp.next
        #     steps -= 1
        # ans = tmp.next
        # tmp.next = None
        # return ans
        """
        除了成环之外，还有快慢指针的做法，在这里因为没有想到，也做个记录。
        首先因为要从首节点走n-k%n-1步，并且获取当前节点的next，所以快指针需要先走k%n步，这样在快指针到尾节点的时候慢指针刚好到前一个节点。
        然后建立环、删除节点联系即可
        """
        fast = head
        length = 0
        while fast:
            length += 1
            fast = fast.next
        fast = head
        for _ in range(k % length):
            fast = fast.next
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        ans = slow.next
        slow.next = None
        return ans
