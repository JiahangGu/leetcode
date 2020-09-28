#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/28 14:19
# @Author:JiahangGu
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        下一个排列的特点是，从最后一位开始向前找应该是升序序列，然后用大于升序结尾前一位数字的最小数字替换该位置，将后面排序，
        并将后面的数字序列逆序填充，最后将前一位原来的数放入到合适的位置
        例如[1,2,5,4,3]，找到从末尾开始的降序为[5,4,3]，则需要替换的数字为2，并且找到最小的大于2的数字为3，得到[1,3,5,4]，
        然后将降序变为升序得到[1,3,4,5]，最后从4开始，将2插入到升序的位置
        """
        idx = len(nums) - 1
        while idx > 0 and nums[idx] <= nums[idx - 1]:
            idx -= 1
        if idx == 0:
            nums.sort()
            return
        x = nums[idx - 1]
        min_idx = len(nums) - 1
        while min_idx > 0 and nums[min_idx] <= x:
            min_idx -= 1
        nums[idx - 1] = nums[min_idx]
        nums.pop(min_idx)
        l, r = idx, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        for i in range(idx, len(nums)):
            if x < nums[i]:
                nums.insert(i, x)
                return
        nums.append(x)


s = Solution()
nums = [5,4,7,5,3,2]
s.nextPermutation(nums)
print(nums)
