#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/22 15:16
# @Author:JiahangGu
from typing import List


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        从右上角开始搜，假设为cur，如果cur<target则向下搜索，cur>target则向左搜索。
        """
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        right = n - 1
        while top < m and right >= 0:
            if matrix[top][right] == target:
                return True
            elif matrix[top][right] > target:
                right -= 1
            else:
                top += 1
        return False


s = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(s.searchMatrix(matrix, 5))
