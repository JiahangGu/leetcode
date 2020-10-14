#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/8 10:30
# @Author:JiahangGu
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        首先为了方便从头遍历以及插入到头结点之前，定义个辅助结点next指向head。
        从第二个结点开始插排，首先取出该节点（设置前驱结点的next），然后从头遍历
        找到插入的合适位置，插入。然后从上次更新的结点开始。
        此外，可以使用一个标记结点记录前一个操作完成后最后一个结点的值，如果待插入结点
        的值大于该节点值，那么直接在该节点后插入并更新即可。
        :param head:
        :return:
        """
        if head == None:
            return None
        tmp = ListNode(0)
        tmp.next = head
        pre, cur = head, head.next
        while cur is not None:
            if cur.val > pre.val:
                cur = cur.next
                pre = pre.next
            else:
                tmpNode = cur.next
                insert_tmp = tmp
                while insert_tmp.next.val < cur.val:
                    insert_tmp = insert_tmp.next
                cur.next = insert_tmp.next
                insert_tmp.next = cur
                cur = tmpNode
                pre.next = cur
        return tmp.next