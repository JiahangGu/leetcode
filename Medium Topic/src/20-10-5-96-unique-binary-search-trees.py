#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/5 10:48
# @Author:JiahangGu

class Solution:
    def numTrees(self, n: int) -> int:
        """
        二叉搜索树的特点是，左子树小于根，右子树大于根。所以对于以k为根节点的二叉搜索树，
        左子树有k-1个结点，右子树有n-k个结点，总的方案就是f(k-1)*f(n-k)。而左子树的k-1个
        结点又是一个k-1个结点构成二叉搜索树的子问题。可以使用记忆化搜索来做。
        而n个结点的树，根节点可以是0-n，所以总的方案数为
        f(n) = f(0) * f(n-1) + f(1) * f(n-2) + ... + f(n-1) * f(0)，
        是卡塔兰数组。
        :param n:
        :return:
        """
        res = [0 for _ in range(n + 1)]
        res[0] = 1
        for i in range(1, n + 1):
            for left in range(i // 2):
                res[i] += res[left] * res[i - left - 1]
            res[i] *= 2
            if (i + 1) % 2 == 0:
                res[i] += res[i // 2] * res[i // 2]
        return res[n]
