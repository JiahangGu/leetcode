#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/11 9:09
# @Author:JiahangGu
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        和之前相比，本题要求只用1-9找出组合数字，并且每个组合不存在重复数字，递归加入对n和k的判断
        并且由小到大遍历即可。
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


s = Solution()
print(s.combinationSum3(3, 9))
