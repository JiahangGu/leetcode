#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 17:10
# @Author:JiahangGu
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        就是在数列二分的基础上扩展到了二维数组。
        仔细看题发现从上到下从左到右得到的数组其实还是一个升序数组，所以就是一个朴素的二分，只是mid计算
        出来之后要映射到行和列。row = mid // len(m[0]), col = mid % len(m[0])。
        :param matrix:
        :param target:
        :return:
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        l, r = 0, m * n - 1
        if matrix[0][0] == target:
            return True
        while l <= r:
            mid = (l + r) // 2
            m_r, m_c = mid // n, mid % n
            # print(m_r, m_c)
            if matrix[m_r][m_c] == target:
                return True
            elif matrix[m_r][m_c] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
