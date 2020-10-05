#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/5 10:49
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
        """
        和96题一样，首先1-n每个都可以作为根节点，并且左子树由小于根节点的结点组成，右子树由大于根节点的结点组成。
        递归生成，递归结束条件是左右子树候选集合均为空。
        首先对于根节点k来说，左子树的生成结果是根节点的列表集合，其中根节点为[1,k-1]范围，而每个根节点又对应
        多种树结构，所以列表中的值可能包含多个相同根节点值但不是同一个根节点的结点。右子树同理。
        所以在递归层面就需要返回List[TreeNode]，因此需要一个list来进行保存。然后对于[1,n]范围来说，1-n均可能
        成为根节点，所以对于每个值都要构建结点list，并以此划分该数的左右子树的结点值范围。
        左右子树方案数为乘法原理，所以需要两层遍历分别得到左右子树的根节点。
        还需要注意的一点是，最终返回的时候，因为要对左右子树进行遍历，所以对于叶子结点来说，左右子树均为None，如果返回
        []的话遍历失败，则叶子结点生成失败，导致最终结果为[]。
        :param n:
        :return:
        """
        def dfs(left, right):
            if left > right:
                return [None]
            ans = []
            for i in range(left, right + 1):
                left_nodes = dfs(left, i - 1)
                right_nodes = dfs(i + 1, right)
                for l in left_nodes:
                    for r in right_nodes:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        ans.append(node)
            return ans

        if n == 0:
            return []
        return dfs(1, n)


s = Solution()
print(s.generateTrees(3))
