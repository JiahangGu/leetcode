#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/5 15:52
# @Author:JiahangGu
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        二叉搜索树所有节点均满足左子树小于根节点，右子树大于根节点。从根节点开始递归查询，如果当前结点
        不满足，返回False，如果满足则继续向左子树和右子树递归查询。
        这个思路有一个缺陷，就是根节点可能和左右子节点是满足，但是子树却不一定满足，这在上述方法中是判断不出的。
        既然要整个子树都满足，那给子树一个上下界即可。只要不在这个范围里，就不符合题意。
        :param root:
        :return:
        """
        # def judge(node, low, up):
        #     if not node:
        #         return True
        #     if node.val <= low or node.val >= up:
        #         return False
        #     return judge(node.left, low, node.val) and judge(node.right, node.val, up)
        #
        # return judge(root, -float('inf'), float('inf'))
        """
        迭代的解法也可以解决，因为中序遍历二叉搜索树会得到一个升序序列，只需要记录前一个数字，如果不满足升序即不符合题意。
        """
        cur = root
        stack = []
        prev = -float('inf')
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev >= cur.val:
                return False
            prev = cur.val
            cur = cur.right
        return True
