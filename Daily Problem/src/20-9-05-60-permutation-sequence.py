#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/5 14:41
# @Author:JiahangGu


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        由于n的最大值只有9，所以可以先回溯求出所有的排列，然后取出第k个返回。
        时间和空间复杂度均为O(n!)。
        :param n:
        :param k:
        :return:
        """
        def premutation(cur, path):
            if cur > n:
                ans.append(path[:])
                return
            for i in range(cur, n):


        ans = []