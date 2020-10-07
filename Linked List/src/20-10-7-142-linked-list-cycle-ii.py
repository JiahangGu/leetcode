#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/7 19:59
# @Author:JiahangGu
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        由于不能使用额外空间，所以考虑双指针解法。首先对问题进行分析，如果存在环，则快慢指针一定会重合，如果不重合则无环。
        当重合时，快慢指针走的步数差为2*x-x=x刚好是环的长度（简单追击问题），知道环的长度之后，对于双指针来说，如果要想
        找到入口，则快慢指针差为环的长度。所以让快指针先走环长的步数，这样在快指针走到入口时，慢指针刚好也到入口。
        上述依然后优化的地方，因为慢指针刚好走了x步，所以slow和head相差x个结点，而不用fast从head重新走。
        实现过程需要注意下对不存在环的判定，如果fast都没有移动过或者移动过但是不等于slow，则不存在环。
        :param head:
        :return:
        """
        fast = head
        slow = head
        step = 0
        while fast and fast.next:
            step += 1
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast != slow or step == 0:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
