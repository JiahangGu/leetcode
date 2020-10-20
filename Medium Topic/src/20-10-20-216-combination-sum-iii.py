#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/20 15:14
# @Author:JiahangGu
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        简单的回溯。要求现有结果含有k项且和刚好为n。
        :param k:
        :param n:
        :return:
        """
        def dfs(left_k, left_n, path, pos):
            if left_k == 0 and left_n == 0:
                ans.append(path[:])
                return
            if left_k == 0 or left_n <= 0:
                return
            for i in range(pos, 10):
                path.append(i)
                dfs(left_k-1, left_n-i, path, i+1)
                path.pop()

        ans = []
        dfs(k, n, [], 1)
        return ans
