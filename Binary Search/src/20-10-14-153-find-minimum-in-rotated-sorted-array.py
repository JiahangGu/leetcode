#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/14 21:23
# @Author:JiahangGu
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        对于有序数组首先想到的就是二分方法。首先，判断nums[0]和nums[-1]的关系，如果0小，那么最小的就是nums[0]。
        否则寻找最小元素。如果mid满足nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]的话，返回。否则根据
        nums[mid]和nums[0]的大小关系，确定最小元素在向左还是向右搜索。需要注意的是，当nums[mid] == nums[0]时，
        且根据上述可知nums[0] > nums[-1]说明是旋转过的，则0不可能是最小值，需要向右搜索。
        :param nums:
        :return:
        """
        if nums[0] < nums[-1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


s = Solution()
nums = [2, 1]
print(s.findMin(nums))
