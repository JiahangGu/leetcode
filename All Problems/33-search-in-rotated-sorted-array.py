#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/28 15:15
# @Author:JiahangGu
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        根据二分减治法的原理，区分什么情况左移，什么情况右移即可。
        首先找到哪半部分是有序的，如果nums[l] < nums[mid]，则左半部分有序，否则右半部分有序。判断是否在有序部分，不在就移动到另一部分
        关键点在于，二分搜索只能在有序序列中进行，所以必须要明确哪部分序列是有序的，并在这个有序序列中判断是否存在。

        此外还有先用二分找到旋转点，然后根据此得到两个有序序列，并进一步查找target的方法，不再实现。
        :param nums:
        :param target:
        :return:
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


s = Solution()
nums = [3,1]
target = 1
print(s.search(nums, target))
