#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/14 23:15
# @Author:JiahangGu
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        首先将-1和n加入到数组中方便处理。然后二分查找峰值（因为峰值一定存在），如果mid满足nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]
        则说明mid是峰值，否则就要根据mid和邻点的关系，向更大的数字方向走，因为爬坡的话一定会遇到一个峰值。
        :param nums:
        :return:
        """
        # nums.insert(0, -1e18)
        # nums.append(1-1e18)
        # l, r = 1, len(nums) - 2
        # while l <= r:
        #     mid = l + (r - l) // 2
        #     if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
        #         return mid - 1
        #     elif nums[mid] < nums[mid + 1]:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        """
        以及减治法。当mid < mid + 1时，说明右边一定存在答案且不是mid，所以右移l=mid+1,。否则左边一定存在答案但不确定mid是否
        是，所以r=mid依然将mid纳入候选范围。
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l


s = Solution()
print(s.findPeakElement([1]))
