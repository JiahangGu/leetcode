#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/30 14:07
# @Author:JiahangGu
from typing import List


class Solution(object):
    def getMaxLen(self, nums):
        """
        首先以0为边界划分为若干段连续非0子数组，找出所有子数组中最大长度即可。子数组长度由负数个数决定，如果负数为偶数个，
        则长度为整个数组长度，如果为奇数，则长度为去除最后一个负数后的子数组和去除第一个负数前的子数组的更大的长度
        :type nums: List[int]
        :rtype: int
        """
        def cal_max_length(neg, s, e):
            if s > e:
                return 0
            if len(neg) & 1 == 1:
                if len(neg) == 1:
                    return max(neg[0] - s, e - neg[0])
                else:
                    return max(neg[-1] - s, e - neg[0])
            else:
                return e - s + 1

        start = 0
        negs = []
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ans = max(ans, cal_max_length(negs, start, i-1))
                start = i+1
                negs = []
                continue
            if nums[i] < 0:
                negs.append(i)
        ans = max(ans, cal_max_length(negs, start, len(nums)-1))
        return ans


s = Solution()
print(s.getMaxLen([1,2,3]))
