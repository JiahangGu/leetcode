#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/11/3 16:21
# @Author:JiahangGu
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        经典dp问题，首先考虑O(n2)的算法。考虑到上升子序列其实是由最后一个数字决定的，如果这个数字
        越小则该序列可能的长度越大，因为新加数字的可能性越高。
        假设dp[i]表示以nums[i]结尾的最长上升子序列，则dp[i] = max(dp[i-k]+1, if nums[i] > nums[k])，
        最终答案为max(dp)，因为任何一个数字都有可能作为结尾。
        :param nums:
        :return:
        """
        # n = len(nums)
        # dp = [1] * n
        # ans = 1
        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[i] > nums[j] and dp[i] < dp[j] + 1:
        #             dp[i] = dp[j] + 1
        #     ans = max(ans, dp[i])
        # return ans
        """
        进阶版要求时间复杂度降低到O(nlgn)，上述n2解法主要的花销在寻找i之前的所有可以添加nums[i]的
        最长子序列中，如果可以在遍历过程中保存对应的信息则可以省略掉这一部分的开销。
        要求最长子序列，且最长子序列是由最后一个数字决定的，可以使用一个数组保存当前的最长子序列，如果
        nums[i]大于该序列的最后一个数字，则最长子序列+1，将该数字放入最后的位置，否则从序列中找一个不影响
        长度的数组进行替换，并且替换之后该位置对应的最长子序列有更好的未来，因为末尾数字更小，后续插入数字的
        可能性越高。并且，替换之后不影响当前最长子序列的长度。替换阶段可以使用二分查找找到第一个大于nums[i]
        的数字并替换为nums[i]
        """
        tail = []
        for i in range(len(nums)):
            if not tail or nums[i] > tail[-1]:
                tail.append(nums[i])
            else:
                l, r = 0, len(tail) - 1
                while l < r:
                    mid = l + (r - l) // 2
                    if tail[mid] >= nums[i]:
                        r = mid
                    else:
                        l = mid + 1
                tail[l] = nums[i]
        return len(tail)


s = Solution()
print(s.lengthOfLIS([4,10,4,3,8,9]))
