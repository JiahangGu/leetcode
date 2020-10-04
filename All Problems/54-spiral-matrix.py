#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 15:53
# @Author:JiahangGu
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        模拟题，从外层开始遍历，直到最内层元素。
        首先从外围开始记录，一圈完成后再深入。
        不过此处有m!=n，所以何时结束遍历需要考虑，也就是需要几圈。
        对于3*5的矩阵，需要两圈，对于5*7的矩阵，需要3圈。
        每一圈遍历之后，剩余矩阵是(m-2)*(n-2)规模。
        遍历结束条件应该是剩余矩阵的规模m,n满足m,n<=0，圈数就是min(m,n)+1//2
        :param matrix:
        :return:
        """
        ans = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        min_mn = min(m, n)
        for k in range((min_mn + 1) // 2):
            # 上层
            for i in range(k, n - k):
                ans.append(matrix[k][i])
            # print(ans)
            # 右层
            if k + 1 >= m - k:
                break
            for i in range(k + 1, m - k):
                ans.append(matrix[i][n - 1 - k])
            # print(ans)
            # 下层
            if k + 1 >= n - k:
                break
            for i in range(k + 1, n - k):
                ans.append(matrix[m - 1 - k][n - 1 - i])
            # print(ans)
            # 左层
            if k + 1 >= m - k - 1:
                break
            for i in range(k + 1, m - k - 1):
                ans.append(matrix[m - 1 - i][k])
            # print(ans)
        return ans