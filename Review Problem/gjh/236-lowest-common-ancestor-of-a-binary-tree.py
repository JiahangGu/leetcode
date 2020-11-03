#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/22 13:57
# @Author:JiahangGu
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        很自然的一个想法是，结合寻找链表的最后公共节点的做法，先一次遍历找到从根节点到q,p的路径作为链表，然后求链表的
        最后公共节点。
        :param root:
        :param p:
        :param q:
        :return:
        """
        # def get_path(node, target, path):
        #     if node == target:
        #         path.append(node)
        #         return True
        #     if not node:
        #         return False
        #     path.append(node)
        #     if node.left:
        #         if get_path(node.left, target, path):
        #             return True
        #     if node.right and get_path(node.right, target, path):
        #         return True
        #     path.pop()
        #     return False
        #
        # path_p, path_q = [], []
        # get_path(root, p, path_p)
        # get_path(root, q, path_q)
        # for i in range(min(len(path_p), len(path_q))):
        #     if path_p[i] != path_q[i]:
        #         return path_p[i - 1]
        # return path_p[-1] if len(path_p) < len(path_q) else path_q[-1]
        """
        除了记录路径的做法之外，还有递归搜索是否包含子节点的做法。对于每一个节点，搜索p, q是否存在于他的子树中。
        假设h(x)表示x是否存在于当前节点的子树中，且lson和rson表示右子节点，则x是最近公共祖先的条件是：
        (h(lson) and h(rson)) or ((x == q or x == p) and (h(lson) or h(rson))
        分别表示p, q存在于x的左右子树中和x是pq中一点，且另一点在子树中。
        """
        def dfs(node, tp, tq):
            nonlocal ans
            if not node:
                return False
            lson = dfs(node.left, tp, tq)
            rson = dfs(node.right, tp, tq)
            if (lson and rson) or ((node == tp or node == tq) and (lson or rson)):
                ans = node
            return lson or rson or node == tp or node == tq

        ans = None
        dfs(root, p, q)
        return ans
