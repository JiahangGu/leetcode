#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/9
# @Author:lulu
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        找到一个升序数组中等于目标值的两个数的下标，必有解
        使用两个指针left和right，left指向第一个数，right指向最后一个数，然后与target比较，如果小于则left右移，如果大于则right左移
        :param numbers:
        :param target:
        :return:

        这个方法本来是想减少第二个二分时的范围，但是在有负数的情况下就错了，比如[-1,0] -1，因为要用到比-1大的数，所以直接做一次二分
        left = 0
        right = len(numbers) - 1
        while left < right:
            mid = left + (right-left+1)//2
            if numbers[mid] > target:
                right = mid - 1
            else:
                left = mid
        flag = left #小于等于target的最大值坐标

        left = 0
        right = flag
        while left < right:
            if numbers[left] + numbers[right] > target:
                right = right - 1
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            else:
                return [left+1,right+1]
        '''

        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right = right - 1
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            else:
                return [left+1,right+1]


s = Solution()
ans = s.twoSum([2,7,11,15],9)
print(ans)
