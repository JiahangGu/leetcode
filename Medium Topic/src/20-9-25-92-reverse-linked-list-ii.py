#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/25 20:27
# @Author:JiahangGu
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        首先从首节点循环m-1次找到要反转的链表区域的前驱结点，然后定义pre=None, cur=翻转链表的
        首节点，两个一对逐个反转，共需反转n-m次。
        注意此方法其实不需要实际新加链表首结点，反转完成后，只需要判断反转前链表区间的前驱结点是否为空，即可得知
        m==1，并且反转后应该以反转区间的链表首节点作为新的head。
        :param head:
        :param m:
        :param n:
        :return:
        """
        if m == n:
            return head
        root = ListNode(0)
        root.next = head
        x = m - 1
        tmp = root
        while x:
            tmp = tmp.next
            x -= 1
        pre, cur = None, tmp.next
        step = n - m + 1
        while step:
            node = cur.next
            cur.next = pre
            pre = cur
            cur = node
            step -= 1
        tmp.next.next = cur
        tmp.next = pre
        return root.next
        """
        上述是迭代解法，下面尝试使用递归的做法完成反转（第一次觉得迭代比递归还简单）。
        反转链表的关键是找到反转区间的左右边界，将边界值互换，然后均向中心点移动，直到二者相邻。
        注意到回溯的过程中，左右边界left和right的处理是不同的，left要向右移动，这是此前不曾到达的，而right向左移动，是通过
        回溯实现的。所以left需要一个全局变量，而right需要作为递归参数用于回溯。并且到达区间中点时，回溯的过程中不能再交换.递归结束
        的条件是right.next==left，因为如果区间是偶数段，则left.next==right时二者并没有交换
        """
        # if not head:
        #     return head
        # left, right = head, head
        # stop = False
        #
        # def back_track(right, m, n):
        #     nonlocal left, stop
        #     if n == 1:
        #         return
        #     right = right.next
        #     if m > 1:
        #         left = left.next
        #     back_track(right, m-1, n-1)
        #     if right == left or left.next == right:
        #         stop = True
        #     if not stop:
        #         left.val, right.val = right.val, left.val
        #         left = left.next
        #
        # back_track(right, m, n)
        # return head
        """
        既然递归可以做，那么也可以使用栈模拟递归。找到开始交换的点，并求出反转区间的长度以及栈的最大深度，在达到之前一直放入左端点，
        到达中点之后，逐个弹出栈顶元素，并与当前右边结点信息互换即可。在栈空时完成反转。不再实现，思路清晰
        """
