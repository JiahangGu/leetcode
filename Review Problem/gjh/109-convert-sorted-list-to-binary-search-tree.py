#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/25 20:27
# @Author:JiahangGu
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        参考有序数组的实现方式：中间结点作为根节点，左边数组作为左子树，右边为右子树，直到建树完成。
        在链表这里可以使用快慢指针寻找中间结点，然后同理之前结点为左子树，之后为右子树。
        时间复杂度O(nlgn)，同合并排序
        :param head:
        :return:
        """
        # def dfs(root):
        #     if not root:
        #         return None
        #     if not root.next:
        #         return TreeNode(root.val)
        #     fast, slow = root, root
        #     pre = None
        #     while fast and fast.next:
        #         pre = slow
        #         fast = fast.next.next
        #         slow = slow.next
        #     node = TreeNode(slow.val)
        #     pre.next = None
        #     left = dfs(root)
        #     right = dfs(slow.next)
        #     node.left = left
        #     node.right = right
        #     return node
        #
        # return dfs(head)
        """
        官方题解给了一个很巧妙的答案，虽然之前也想过但是没有想到具体的实现方法，主要解决的是链表无法快速获得中间结点的问题。
        思路是这样：二叉搜索树的中序遍历结果是一个有序的序列，逆向思考的话，如果建好一个二叉搜索树，并已知中序遍历结果，
        那么只需要将有序序列填入相应位置即可。相应的建树方式和上述一样，只不过root会在左子树遍历完成后填入。
        时间复杂度为O(n)，等于中序遍历的复杂度。关键点在于head是一个全局变量，指向当前的链表结点
        """
        def dfs(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode()
            root.left = dfs(left, mid-1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = dfs(mid+1, right)
            return root

        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        return dfs(0, length-1)
