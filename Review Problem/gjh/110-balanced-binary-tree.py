#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/28 22:40
# @Author:JiahangGu


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        自顶向下的解法，对于每个非叶子节点，求出左右子节点的高度比较是否平衡，但会存在
        求高度的函数多次调用的情况，最坏情况下n个节点形成链表，每个节点访问到是O(N)，且每
        个节点求高度需要N+N-1+...+1，总复杂度为O(N2)
        采用自底向上的解法可以避免重复调用，先比较左右子节点对应的子树高度是否平衡，均平衡
        的情况下再判断当前节点是否平衡，但需要解决同时求高度并且标记是否平衡的情况
        TIPS：可以使用数字标记，如果不平衡返回-1，如果平衡返回高度，高度是不可能出现-1的，
        所以可以作为不平衡的情况
        :param root:
        :return:
        """
        def get_depth(r):
            if not r:
                return 0
            left_depth = get_depth(r.left)
            right_depth = get_depth(r.right)
            if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
                return -1
            return max(left_depth, right_depth) + 1
        return get_depth(root) >= 0
