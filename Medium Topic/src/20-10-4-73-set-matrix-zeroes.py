#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 17:05
# @Author:JiahangGu
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        按照题目要求来做，如果使用O(mn)空间，复制矩阵即可。
        使用O(m+n)空间，使用两个list记录行和列被置为0的索引。
        使用常数空间的话，如果出现了0，将行首和列首元素置为0，表明该行或该列需要被置为0。而0,0这个位置
        因为具有重叠性，需要一个单独的标记来记录是0行还是0列应该被置为0.
        """
        flag_row = 0
        flag_col = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        flag_row = 1
                    if j == 0:
                        flag_col = 1
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        print(matrix)
        for i in range(m - 1, 0, -1):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for i in range(n - 1, 0, -1):
            if matrix[0][i] == 0:
                for j in range(m):
                    matrix[j][i] = 0
        if flag_row == 1:
            for i in range(n):
                matrix[0][i] = 0
        if flag_col == 1:
            for i in range(m):
                matrix[i][0] = 0
