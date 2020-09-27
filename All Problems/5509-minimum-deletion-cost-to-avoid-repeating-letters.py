#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/6 10:54
# @Author:JiahangGu
from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        def get_min_sum(arr):
            return sum(arr) - max(arr)

        i = 0
        ans = 0
        while i < len(s):
            char = s[i]
            j = i
            while j < len(s) and s[j] == char:
                j += 1
            if j - i > 1:
                ans += get_min_sum(cost[i:j])
            i = j
        return ans


s = Solution()
cost = [1,2,3,4,1]
print(s.minCost("aabaa", cost))
