#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/8 9:44
# @Author:JiahangGu
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        后序遍历对子节点的遍历顺序是前序的逆序，所以优先放入左子节点，再放入右子节点，得到的结果即是
        后序遍历的逆序。
        :param root:
        :return:
        """
        # if not root:
        #     return []
        # ans = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     ans.append(node.val)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return ans[::-1]
        """
        后序遍历在栈的模拟过程中，需要注意先访问完左右子节点才最后访问根节点，所以在保存当前结点
        的值之前，需要先判断子节点是否为空或者已访问过。这在栈模拟中来说不好只通过栈做到，因为访问
        完左子节点之后，还需要先访问右子节点，如果按照之前的做法，第一次回溯到根节点时会被弹出，所以
        改进的方法是，首先根节点不会在回溯时立即弹出，其次使用一个前驱结点，记录之前访问的结点，如果
        当前结点的子节点为空，或者该节点的右子节点为记录好的前驱结点，表明该节点子节点访问完成，弹出
        栈并记录该节点值。
        """
        cur = root
        stack = []
        ans = []
        prev = None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack[-1]
            if not cur.right or cur.right == prev:
                ans.append(cur.val)
                stack.pop()
                prev = cur
                cur = None
            else:
                cur = cur.right
        return ans
