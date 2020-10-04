#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 15:26
# @Author:JiahangGu
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        从外层开始一层层替换即可，主要是模拟。此外需要申请一个O(n)的列表存储被替换的元素。
        """
        n = len(matrix)
        for i in range(n // 2):
            res = []
            # 记录上层
            for j in range(i, n - i):
                res.append(matrix[i][j])
            # print(res)
            # 移动左层
            for j in range(i, n - i):
                matrix[i][n - 1 - j] = matrix[j][i]
            # print(matrix)
            # 移动下层
            for j in range(i, n - i):
                matrix[j][i] = matrix[n - i - 1][j]
            # print(matrix)
            # 移动右层
            for j in range(i, n - i):
                matrix[n - i - 1][j] = matrix[n - 1 - j][n - i - 1]
            # print(matrix)
            # 移动左层
            k = 0
            for j in range(i, n - i):
                matrix[j][n - 1 - i] = res[k]
                k += 1
            # print(matrix)
