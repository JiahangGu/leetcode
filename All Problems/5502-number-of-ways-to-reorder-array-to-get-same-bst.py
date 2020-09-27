#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/30 14:18
# @Author:JiahangGu
from typing import List


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        """
        首先要明确解题的关键：BST的性质（不再赘述)，决定了相同的BST一定具有相同的根节点，并且
        在插入元素时左右子树的节点顺序必须相同，也就意味着在这里，数组元素的顺序只要保证在左右子
        树的相对顺序一致，而在整个树的顺序可以打乱，即小于根节点的数列顺序和大于根节点的数列顺序
        保持不变。这样在len(nums)-1个位置中只要选择left个位置填入左子树的节点，left表示左子树
        的节点个数，求解形式为C(len(nums)-1, left)。这只是以BST的根节点为根节点的情况，而实际
        递归的左子树和右子树也具有类似的情况，即递归进入的情况应该以第一个数字为根节点，求解对应的
        情况个数，而为什么要用第一个数字为根节点呢？很简单，要保持左右子树的数组序列保持不变，第一个
        数字一定是根节点。不是第一个数字的元素要作为根节点只能选择其后的数字作为子节点。
        :param nums:
        :return:
        """
        import math

        def divide_conquer(nodes):
            if not nodes or len(nodes) == 1:
                return 1
            root = nodes[0]
            left = [x for x in nodes if x < root]
            right = [x for x in nodes if x > root]
            return combine(len(nodes)-1, len(left)) * divide_conquer(left) * divide_conquer(right) % MOD

        def combine(n, m):
            return math.factorial(n)//(math.factorial(m)*math.factorial(n-m))

        MOD = 10 ** 9 + 7
        return divide_conquer(nums) - 1


s = Solution()
print(s.numOfWays([9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]))
