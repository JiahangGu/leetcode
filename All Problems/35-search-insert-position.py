#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/17 9:14
# @Author:JiahangGu
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        使用二分减治法解决二分，具体解释见二分文档
        nums[mid] < target时可以得知，mid和mid左侧的数据都不可能满足题解，所以要去右边搜索可行解
        :param nums:
        :param target:
        :return:
        '''
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            # 如果target>nums[mid]，[left, mid]排除，[mid+1, right]
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left


s = Solution()
x = [1,3,5,6]
print(s.searchInsert(x, 5))
