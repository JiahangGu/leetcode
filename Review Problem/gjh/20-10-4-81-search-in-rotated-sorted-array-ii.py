#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 20:48
# @Author:JiahangGu
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        这道题在之前的旋转数组上新增加了可能出现重复元素的条件。相比上一道题，新增加了一种新的情况，
        就是可能存在nums[l] == nums[mid]的情况，对于这种情况，要么[l,mid]是全部相等，要么[mid,r]
        是全部相等，但是无法确定具体是哪一个，例如[1,3,1,1,1]和[1,1,1,3,1]两种。对于这种情况，只能得到
        nums[l]不是target的结论，而不知道是向左还是向右搜索，所以只能令l+=1，排除l这个错误选项。
        时间复杂度最坏情况下会变成O(N)。
        :param nums:
        :param target:
        :return:
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            elif nums[l] == nums[mid]:
                l += 1
            elif nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


s = Solution()
print(s.search([2,4,5,0,0,1,2], 1))
