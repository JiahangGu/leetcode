#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/7 8:04
# @Author:JiahangGu


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        '''
        :DFS记录当前路径和，如果当前和为目标值且当前节点是叶子节点，返回路径。回溯过程中要减去此前加上的节点
        值，确保回溯到其余路径时节点值不包含其他路径。
        注意：只需要找到一条路径即可，并且节点值可能为负值，这里不存在剪枝的条件。
        :param root:
        :param sum:
        :return:
        '''

        # def dfs(cur_node, cur_sum):
        #     if cur_sum + cur_node.val == sum and cur_node.left is None and cur_node.right is None:
        #         return True
        #     cur_sum += cur_node.val
        #     if cur_node.left:
        #         if dfs(cur_node.left, cur_sum):
        #             return True
        #     if cur_node.right:
        #         if dfs(cur_node.right, cur_sum):
        #             return True
        #     cur_sum -= cur_node.val
        #     return False
        #
        # if not root:
        #     return False
        # return dfs(root, 0)

        '''
        函数优化：不需要新建函数统计当前的路径和，而是可以在原函数上比较剩余路径和，比如hasPathSum(root, sum)
        就可以看作是从root开始，还需要凑齐的路径和为sum。如果某一叶子节点时sum为0则存在路径和。
        '''
        if not root:
            return False
        if root.left is None and root.right is None:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


def test_case():
    pass
