#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/21 9:05
# @Author:JiahangGu
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        '''
        注意这道题和此前一道求数量的题目区别，求数量是dp求卡特兰数列，而这个是求所有
        解，是一个搜索的问题，dp的标签有些误导。
        本题关键和dp一样，在于二叉搜索树的根节点大于左子树所有节点，小于右子数所有节
        点，所以选定n和根之后，可以确定左右子树的数值范围，也就可以确定对应的排列。
        另一个问题是答案中null的处理，我一直觉得leetcode的null很迷，在这里较好判断，
        由于是给定左右子树的数值范围，当范围不存在即start>end时形成一个空节点，表示
        该树不存在。
        :param n:
        :return:
        '''
        def dfs(start, end):
            if start > end:
                return [None, ]
            allTrees = []
            for i in range(start, end+1):
                leftTrees = dfs(start, i-1)
                rightTrees = dfs(i+1, end)
                for l in leftTrees:
                    for r in rightTrees:
                        rootNode = TreeNode(i)
                        rootNode.left = l
                        rootNode.right = r
                        allTrees.append(rootNode)
            return allTrees
        return dfs(1, n)


s = Solution()
print(s.generateTrees(3))
