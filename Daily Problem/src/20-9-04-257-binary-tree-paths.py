#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/4 15:36
# @Author:JiahangGu
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """
        直接从根节点遍历，到叶子节点的时候记录路径就完事了
        :param root:
        :return:
        """
        def construct_ans(path):
            ans = ""
            for n in path:
                ans += str(n)
                ans += "->"
            return ans[:-2]

        def dfs(node, path):
            if not node.left and not node.right:
                path.append(node.val)
                ans.append(construct_ans(path))
                path.pop()
                return
            path.append(node.val)
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
            path.pop()

        if not node:
            return []
        ans = []
        dfs(root, [])
        return ans


s = Solution()
print(s.binaryTreePaths())
