#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/20 21:37
# @Author:JiahangGu
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        双指针遍历，和大左移，和小右移
        :param numbers:
        :param target:
        :return:
        '''
        left, right = 0, len(numbers)-1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]


s = Solution()
x = [2, 7, 11, 15]
print(s.twoSum(x, 9))
