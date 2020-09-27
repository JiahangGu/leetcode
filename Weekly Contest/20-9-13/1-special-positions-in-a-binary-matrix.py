#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/15 9:30
# @Author:JiahangGu
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        字典统计行列出现过1的次数。
        :param mat:
        :return:
        """
        from collections import defaultdict
        pos_row, pos_col = defaultdict(int), defaultdict(int)
        m = len(mat)
        n = len(mat[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    pos_row[i] += 1
                    pos_col[j] += 1
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and pos_row[i] == 1 and pos_col[j] == 1:
                    ans += 1
        return ans


s = Solution()
mat = [[0,0,0,0,0],
            [1,0,0,0,0],
            [0,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]]
print(s.numSpecial(mat))
