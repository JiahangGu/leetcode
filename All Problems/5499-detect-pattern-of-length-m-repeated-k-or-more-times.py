#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/30 14:11
# @Author:JiahangGu
from typing import List


class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        遍历每一个起点，判断长度为i的子模式是否出现k次即可
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        arr = "".join([str(x) for x in arr])
        for i in range(len(arr)-m):
            cur = i
            num = 1
            while cur+m+m <= len(arr) and arr[cur:cur+m] == arr[cur+m:cur+m+m]:
                num += 1
                cur += m
            if num >= k:
                return True
        return False