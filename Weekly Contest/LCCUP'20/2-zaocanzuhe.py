#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/14 11:03
# @Author:JiahangGu
from typing import List


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        """
        排序，对于所有早餐价格，二分查找小于等于剩余价格的最右边索引，则左边所有的都是满足条件的，计算个数。
        :param staple:
        :param drinks:
        :param x:
        :return:
        """
        def binary_search(nums, target):
            if target < nums[0]:
                return -1
            l, r = 0, len(nums) - 1
            while l < r:
                mid = l + (r - l + 1) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] <= target:
                    l = mid
            return l

        staple.sort()
        drinks.sort()
        ans = 0
        for price in staple:
            idx = binary_search(drinks, x - price)
            ans = (ans + idx + 1) % (10 ** 9 + 7)
        return ans


s = Solution()
staple = [2,1,1]
drinks = [8,9,5,1]
x = 9
print(s.breakfastNumber(staple, drinks, x))
