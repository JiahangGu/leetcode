#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 17:19
# @Author:JiahangGu
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        荷兰国旗问题，将三种颜色，一种放在最前面，一种在中间，另一种在最后面。
        可以使用类似于partition的方法，使用两个指针，将所有第一种放到第一部分，最后一种放大第三部分，则中间为第二部分。
        """
        if nums == []:
            return nums
        length = len(nums)
        index_0 = 0
        index_2 = length - 1
        i = 0
        while i <= index_2:
            if nums[i] == 2:
                nums[i] = nums[index_2]
                nums[index_2] = 2
                index_2 -= 1
            elif nums[i] == 0:
                nums[i] = nums[index_0]
                nums[index_0] = 0
                index_0 += 1
                i += 1
            else:
                i += 1
