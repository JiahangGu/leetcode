#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 16:49
# @Author:JiahangGu
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        类似前一个旋转矩阵的做法，模拟。只不过这个题是给定的数字要求生成，思路都是一样的，从外层开始生成，到最内层结束。
        :param n:
        :return:
        """
        ans = [[-1 for _ in range(n)] for _ in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r, c, di = 0, 0, 0
        cur = 1
        for _ in range(n ** 2):
            ans[r][c] = cur
            cur += 1
            rr = r + dr[di]
            cc = c + dc[di]
            if 0 <= rr < n and 0 <= cc < n and ans[rr][cc] == -1:
                r = rr
                c = cc
            else:
                di = (di + 1) % 4
                r += dr[di]
                c += dc[di]
        return ans
