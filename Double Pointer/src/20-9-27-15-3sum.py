#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/27 18:42
# @Author:JiahangGu
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        首先尝试下O(n^2)的解法。参考两数之和中双指针的解法，对于每个数字，使用双指针求解所有可行解。并且
        排序好的序列做去重只要排除第一个数字已经出现过的情况即可。
        此外，所有的凑数问题都可以使用这种解法。并且时间复杂度是完全可以接受的
        :param nums:
        :return:
        """
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) - 1 and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while r > 0 and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return ans


s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))
