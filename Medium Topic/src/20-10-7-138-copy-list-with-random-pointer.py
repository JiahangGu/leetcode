#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/7 16:58
# @Author:JiahangGu
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        问题的难点在于，深拷贝之后要为随机指针赋值，如果采用常规的拷贝做法，形成链式关系之后为新生成的
        链表结点赋随机指针时需要对原链表进行遍历。所以一个想法就是可以构建出原链表到新生成链表的关系，
        这样在赋值随机指针时可以根据原结点的随即指针直接找到新生成的结点。
        一个做法就是，生成新链表结点作为原结点的next，形成old-new-old-new的结构，可以直接找到对应结点。
        :param head:
        :return:
        """
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = cur.next.next
        cur = head
        while cur:
            cur.next.random = cur.random.next
            cur = cur.next.next
        return head
