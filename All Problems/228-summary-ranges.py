#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/21 9:35
# @Author:JiahangGu
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        统计连续自然数的出现范围。单指针遍历，如果相邻数差1则是一个区间内，否则更新区间范围。
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return []
        l, r = 0, 0
        ans = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                r += 1
            else:
                if l == r:
                    ans.append(str(nums[l]))
                else:
                    ans.append(str(nums[l]) + "->" + str(nums[r]))
                l = r = i
        if l == r:
            ans.append(str(nums[l]))
        else:
            ans.append(str(nums[l]) + "->" + str(nums[r]))
        return ans
