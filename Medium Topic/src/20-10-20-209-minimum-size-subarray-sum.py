#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/20 11:21
# @Author:JiahangGu
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        滑动窗口，如果窗口内数字和>=s，更新解，并且左侧指针+1，如果不满足则右侧指针+1，对应更新窗口内的和。
        :param s:
        :param nums:
        :return:
        """
        if sum(nums) < s:
            return 0
        l = r = 0
        ans = len(nums)
        cur_sum = 0
        i = 0
        while i < len(nums):
            if cur_sum >= s:
                ans = min(ans, i - l)
                cur_sum -= nums[l]
                l += 1
            else:
                cur_sum += nums[i]
                i += 1
        while cur_sum >= s:
            ans = min(ans, i - l)
            cur_sum -= nums[l]
            l += 1
        return ans
