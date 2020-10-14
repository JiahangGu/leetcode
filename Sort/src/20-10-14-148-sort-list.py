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
        归并排序。归并时不能使用新建数组存储，而是要在本地修改。
        首先将链表划分为两个子表，设为s1和s2开头的，且s1的末尾的next为None(在找到s2之后设置）
        递归结束条件为s1.next == None（表明当前结点为唯一一个结点）
        :param head:
        :return:
        """
        def merge(head1, head2):
            root1 = ListNode(0)
            root1.next = head1
            root = root1
            while root1.next and head2:
                while root1.next and root1.next.val < head2.val:
                    root1 = root1.next
                node = head2.next
                head2.next = root1.next
                root1.next = head2
                head2 = node
                root1 = root1.next
            if head2:
                root1.next = head2
            return root.next

        def merge_sort(head):
            if not head:
                return None
            if not head.next:
                return head
            fast, slow = head, head
            prev = None
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
            prev.next = None
            h1 = merge_sort(head)
            h2 = merge_sort(slow)
            root = merge(h1, h2)
            return root

        return merge_sort(head)


n1 = ListNode(4)
n2 = ListNode(2)
n3 = ListNode(1)
n4 = ListNode(3)
n1.next = n2
n2.next = n3
n3.next = n4
s = Solution()
ans = s.sortList(n1)
print(ans.val)
