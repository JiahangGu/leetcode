#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/27 20:43
# @Author:JiahangGu
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        和15题一样，只不过将之前找target变成找和target差最小的三个数字，双指针解法一样。在差更小时更新解。
        :param nums:
        :param target:
        :return:
        """
        ans = 0
        tmp = 1e18
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if abs(nums[i] + nums[l] + nums[r] - target) < tmp:
                    tmp = abs(nums[i] + nums[l] + nums[r] - target)
                    ans = nums[i] + nums[l] + nums[r]
                if nums[i] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return ans


s = Solution()
print(s.threeSumClosest([0,2,1,-3], 1))
