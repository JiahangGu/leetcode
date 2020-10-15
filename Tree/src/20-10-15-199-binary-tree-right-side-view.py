#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/15 16:49
# @Author:JiahangGu
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        层次遍历，返回每一层最右边的结点。也可以DFS搜索过程将所有结点及其对应的高度记录下来，遍历所有高度
        并取出最右边的结点。
        :param root:
        :return:
        """
        # def print(root, d, depth):
        #     if root is None:
        #         return
        #     d[depth].append(root.val)
        #     print(root.left, d, depth + 1)
        #     print(root.right, d, depth + 1)
        #
        # if root is None:
        #     return []
        # from collections import defaultdict
        # d = defaultdict(list)
        # depth = 0
        # print(root, d, depth)
        # res = []
        # for key in d.keys():
        #     res.append(d[key][-1])
        # return res
        """
        层次遍历解法
        """
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            num = len(queue)
            idx = 0
            while idx < num:
                node = queue.pop(0)
                if idx == 0:
                    ans.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                idx += 1
        return ans

