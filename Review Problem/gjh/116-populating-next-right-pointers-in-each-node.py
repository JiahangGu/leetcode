#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/26 22:29
# @Author:JiahangGu
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        分析同117题，只是这里给定是完美二叉树，不需要判断left、right是否存在
        :param root:
        :return:
        """
        # cur = root
        # while cur:
        #     dumm = Node()
        #     pre = dumm
        #     while cur:
        #         if cur.left:
        #             pre.next = cur.left
        #             pre = pre.next
        #         if cur.right:
        #             pre.next = cur.right
        #             pre = pre.next
        #         cur = cur.next
        #     cur = dumm.next
        # return root
        """
        对于问题本身来说，如果不考虑117题，这个完美二叉树可以直接赋予next。如果当前结点是左子节点，则next为父节点的右子节点，
        如果当前结点是右子节点，则next为父节点的next的左子节点。因为不存在需要判断为空的情况。
        并且通过这里也发现题目之间是有关系的，决定从下一题开始从头开始，此前刷过的也再来一遍，放在这个专题下
        """
        if not root:
            return None
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root