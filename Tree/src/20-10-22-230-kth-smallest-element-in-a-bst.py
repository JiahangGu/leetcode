#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/22 11:26
# @Author:JiahangGu
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        O(N)解法中序遍历得到有序数组，返回第k个元素。
        :param root:
        :param k:
        :return:
        """
        # nodes = []
        # stack = []
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     nodes.append(root.val)
        #     root = root.right
        # return nodes[k - 1]
        """
        上述算法需要在每次检查都得到所有的结点然后才返回结果，时间复杂度较高。
        但是看官方题解貌似，也就是这种解法，不过是不记录所有节点，空间复杂度优化到O(h)，h是树的高度。
        这样的时间复杂度也做不到提示里提到的O(h)，而是O(k)，平均下k为1-n依然是O(n)。不懂
        """
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
