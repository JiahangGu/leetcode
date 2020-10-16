#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/15 16:41
# @Author:JiahangGu
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        难点是这道题要求使用三种空间复杂度为O(1)的解法。首先所有方法都要求一个k % n表示实际需要移动的位置
        """
        """
        第一种方法，模拟。在移动位置到0之前，将整个数组向右移动一个位置，时间复杂度为O(nk)，太高了。
        """
        """
        第二种方法，也是模拟，但是每次直接将数字移动到目标位置，例如移动k个位置时，0移动到k，1
        移动到k+1，直到移动完所有的数字，这样只需要一个临时变量存储即可。
        """
        n = len(nums)
        k %= n
        cnt = 0
        idx = -1
        while cnt < n:
            flag = True
            idx += 1
            start_idx = idx
            target = nums[idx]
            while start_idx != idx or flag:
                target_idx = (start_idx + k) % n
                tmp = nums[target_idx]
                flag = False
                nums[target_idx] = target
                start_idx = target_idx
                target = tmp
                cnt += 1
        """
        第三种方法，python的切片，直接找到分割的位置将后半部分移动到前半部分。这种是使用语言特性，严格来说
        算不上一种方法，但是想到了就写上了。
        """
        """
        第四种方法，数组反转。找到要成为第一个数字的位置即n-k，则将数组划分为[0:n-k-1]和[n-k:n-1]两个子数组，
        分别将两个数组反转，记得到目标数组的逆序，再将整个数组反转即可得到结果。
        """
        # def reverse(start, end):
        #     while start < end:
        #         nums[start], nums[end] = nums[end], nums[start]
        #         start += 1
        #         end -= 1
        #
        # n = len(nums)
        # k %= n
        # mid = n - k
        # reverse(0, mid - 1)
        # reverse(mid, n - 1)
        # reverse(0, n - 1)


s = Solution()
nums = [1,2,3,4,5,6]
s.rotate(nums, 3)
print(nums)
