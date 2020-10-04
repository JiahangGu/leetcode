#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 20:43
# @Author:JiahangGu
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        遍历，统计当前数字出现的次数，如果出现了两次以上，直接删除掉多余的。
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return 0
        start = 0
        # cur = nums[0]
        freq = 1
        length = len(nums)
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                freq += 1
                i += 1
            else:
                if freq > 2:
                    for j in range(2, freq):
                        nums.pop(start)
                    i = start + 2
                    start = start + 2
                else:
                    start = i
                    i += 1
                freq = 1
        if freq > 2:
            for j in range(2, freq):
                nums.pop(start)
        return len(nums)
    