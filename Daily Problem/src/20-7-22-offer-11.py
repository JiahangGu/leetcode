#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/22 8:04
# @Author:JiahangGu
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        '''
        这题的关键点在于区分前一段还是后一段的上升序列，根据当前范围的右端点可以确定是在左还是右，
        if nums[mid] < nums[right] 则答案一定是在mid的左边序列，right = mid
        elif nums[mid] > nums[right] 则答案一定是在mid的右边序列，left = mid+1
        有一个特殊情况是nums[mid]==nums[right]时答案是在左边但是不能确定位置，因为可能是连续相等
        的序列也可能是在左边，但如果合并到前面的第一个case又会死循环，所以特别处理。
        :param numbers:
        :return:
        '''
        if numbers[0] < numbers[-1]:
            return numbers[0]
        l, r = 0, len(numbers)-1
        while l < r:
            mid = l + (r-l)//2
            if numbers[mid] < numbers[r]:
                r = mid
            elif numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] == numbers[r]:
                r -= 1
        return numbers[l]


s = Solution()
x = [2,2,2,0,1]
print(s.minArray(x))
