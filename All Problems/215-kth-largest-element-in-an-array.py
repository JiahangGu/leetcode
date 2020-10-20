#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/20 14:24
# @Author:JiahangGu
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        利用快排的思想，将数组划分为[>mid:mid:<mid]，得到mid之后与k作对比，如果大于k则说明第k大元素
        在左部分，则进入左部分查找，否则进入右部分。
        注意这里选择哨兵时需要随机选择，否则很容易达到最坏情况复杂度。
        :param nums:
        :param k:
        :return:
        """
        import random
        def partition(l, r):
            if l > r:
                return -1
            idx = random.randint(l, r)
            nums[l], nums[idx] = nums[idx], nums[l]
            tmp = nums[l]
            start = l
            end = r
            while start < end:
                while start < end and nums[end] < tmp:
                    end -= 1
                if start < end:
                    nums[start] = nums[end]
                while start < end and nums[start] >= tmp:
                    start += 1
                if start < end:
                    nums[end] = nums[start]
            nums[start] = tmp
            return start

        l, r = 0, len(nums) - 1
        k -= 1
        while True:
            mid = partition(l, r)
            if mid == k:
                return nums[mid]
            elif mid > k:
                r = mid - 1
            else:
                l = mid + 1


s = Solution()
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
