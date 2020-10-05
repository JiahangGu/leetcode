#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/5 17:11
# @Author:JiahangGu
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        层次遍历可以参考模板题，这个是在此基础上的扩展。
        一种方案是记录层数，在记录需要逆序的层的结果是存逆序结果。
        另一种是使用双端队列的做法，是在记录该层值的时候，如果是逆序的则将该节点值插到该层结果的首元素中，
        即BFS遍历方式不变，但是在存储的时候插入到第一位来实现逆序的效果。
        DFS解法也同理，在逆序的时候逆着插。
        :param root:
        :return:
        """
        if not root:
            return []
        q = [root]
        level = []
        level_num = True
        while q:
            cur_level = []
            num = len(q)
            while num:
                node = q.pop(0)
                cur_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                num -= 1
            if level_num:
                level.append(cur_level)
            else:
                level.append(cur_level[::-1])
            level_num = not level_num
        return level
