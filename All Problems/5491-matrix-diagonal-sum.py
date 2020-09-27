#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/5 22:41
# @Author:JiahangGu
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n == 0:
            return 0
        ans = 0
        i, j = 0, n-1
        while i < n:
            ans += mat[i][i]
            ans += mat[i][j]
            i += 1
            j -= 1
        if n & 1 == 1:
            ans -= mat[n//2][n//2]
        return ans


s = Solution()
print(s.diagonalSum([[5]]))
