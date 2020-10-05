#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/5 10:07
# @Author:JiahangGu
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        中序遍历顺序为左子节点-根节点-右子节点。
        迭代算法，首先找到最深层的左子节点，并将路径中的所有节点入栈。然后弹出栈顶节点就是当前节点，记录。如果
        该节点具有右子节点，放入右子节点。
        :param root:
        :return:
        """
        # if not root:
        #     return []
        # stack = [root]
        # ans = []
        # cur = root
        # while stack:
        #     while cur.left:
        #         stack.append(cur.left)
        #         cur = cur.left
        #     cur = stack.pop()
        #     ans.append(cur.val)
        #     cur.left = None
        #     if cur.right:
        #         stack.append(cur.right)
        #         cur = cur.right
        # return ans
        """
        另一种写法
        """
        # stack = []
        # ans = []
        # cur = root
        # while stack or cur:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     ans.append(cur.val)
        #     cur = cur.right
        # return ans
        """
        Morris中序遍历，空间复杂度减小到O(1)，主要是利用前驱结点和后继结点的特点实现中序遍历。
        对于当前结点，找到其前驱结点，即左子树中最右侧的结点，如果该节点的右子节点为空，说明还没有访问到，
        将右子节点赋值为当前结点，以待后续回溯使用，并进入左子节点进入后续遍历。
        总结可以分为下述两种情况
        if cur.left is None:
            cur.val
            cur = cur.right
        else:
            prev = cur.left
            while prev.right != None and prev != cur:
                prev = prev.right
            if prev.right == None:
                prev.right = cur
                cur = cur.left
            else:
                cur.val
                prev.right = None
                cur = cur.right
        """
        cur = root
        ans = []
        while cur:
            if cur.left is None:
                ans.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    ans.append(cur.val)
                    prev.right = None
                    cur = cur.right
        return ans
