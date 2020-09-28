#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/28 16:25
# @Author:JiahangGu
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        两次二分即可。减治法。
        时target < nums[mid]， r =
        :param nums:
        :param target:
        :return:
        """
        if len(nums) == 0:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[l] != target:
            return [-1, -1]
        ans_l = l
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        ans_r = r
        return [ans_l, ans_r]