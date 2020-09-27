#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/6 13:40
# @Author:JiahangGu
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        q = [root]
        level = []
        cur_level = []
        cur_level_num = 1
        next_level_num = 0
        while q:
            node = q.pop(0)
            cur_level.append(node.val)
            if node.left:
                next_level_num += 1
                q.append(node.left)
            if node.right:
                next_level_num += 1
                q.append(node.right)
            cur_level_num -= 1
            if cur_level_num == 0:
                level.append(cur_level)
                cur_level = []
                cur_level_num = next_level_num
                next_level_num = 0
        return level
