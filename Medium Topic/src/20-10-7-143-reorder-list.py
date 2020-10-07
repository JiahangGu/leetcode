#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/7 20:57
# @Author:JiahangGu
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        首先就是O(N)空间复杂度的解法，先全部存起来，然后做结点的串联。
        但是觉得肯定不是这个做法，不像是中等题解法。
        思考其余解法，递归可以实现，因为递归可以得到之前遍历过的结点，但空间复杂度也是O(N)，但有些难度，尝试实现。
        首先设定一个head指向从左开始的当前结点，这个是全局变量只有修改next之后才会修改。然后一路干到最后一个结点，
        找到最后一个结点后开始修改链接。递归终止条件是遇到中间结点或者中间两个结点。此外由于会一直回溯，最后会修改前半部分
        结点的连接关系，所以在递归终止时定义一个标记，表明已经反转完成。
        """
        # def dfs(tail):
        #     nonlocal tmp, flag
        #     if not tail:
        #         return
        #     dfs(tail.next)
        #     if flag:
        #         return
        #     if tail == tmp or tmp.next == tail:
        #         tail.next = None
        #         flag = True
        #         return
        #     tail.next = tmp.next
        #     tmp.next = tail
        #     tmp = tail.next
        #
        # tmp = head
        # flag = False
        # dfs(head)
        """
        递归解法依然需要O(N)复杂度来开递归栈，所以空间并没有优化。思考一下有没有O(1)的解法。
        观察链表的规律，发现是从左边取第一个，然后从右边取第一个，然后左边第二个，右边第二个。。。所以只要找到
        后半部分链表，并反转，就得到了后半部分的逆序。有了逆序链表就可以左右同时取第一个节点构造新链表关系。
        所以首先双指针找到中间结点，对后半部分进行反转，然后合并两个链表。nice
        """
        if not head:
            return
        fast, slow = head, head
        slow_prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow_prev = slow
            slow = slow.next
        # 右半部分链表的起点
        if fast:
            begin = slow.next
            slow.next = None
        else:
            begin = slow
            slow_prev.next = None
        prev = None
        while begin:
            tmp = begin.next
            begin.next = prev
            prev = begin
            begin = tmp
        while prev and head:
            tmp_prev = prev.next
            prev.next = head.next
            head.next = prev
            head = prev.next
            prev = tmp_prev


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
s = Solution()
s.reorderList(n1)
