#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/14 15:29
# @Author:JiahangGu
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        首先0将数组划分为若干个不相连的子数组，因为含0的子数组乘积都是0.
        然后统计每个子数组的最大乘积。首先如果是偶数个负数，那么这个就是最大值，如果是奇数个负数，则需要判断抛弃第一个负数
        之前的所有数字的乘积大还是抛弃最后一个负数之后的所有数字的乘积大。
        :param nums:
        :return:
        """
        # def get_max(arr, num):
        #     if len(arr) == 1:
        #         return arr[0]
        #     if num & 1:
        #         dp = [1] * (len(arr) + 1)
        #         start, end = -1, -1
        #         for i in range(len(arr)):
        #             dp[i + 1] = dp[i] * arr[i]
        #             if arr[i] < 0:
        #                 if start == -1:
        #                     start = i
        #                 end = i
        #         ans = max(dp[-1] // dp[start + 1], dp[end])
        #     else:
        #         ans = 1
        #         for n in arr:
        #             ans *= n
        #     return ans
        #
        # ans = -1e18
        # idx = 0
        # seq = []
        # start = 0
        # end = -1
        # num_neg = 0
        # while idx < len(nums):
        #     if nums[idx] == 0:
        #         ans = max(ans, 0)
        #         seq.append((start, end, num_neg))
        #         while idx < len(nums) and nums[idx] == 0:
        #             idx += 1
        #         if idx == len(nums):
        #             break
        #         start = idx
        #         end = idx
        #         num_neg = 0
        #     else:
        #         if nums[idx] < 0:
        #             num_neg += 1
        #         end = idx
        #         idx += 1
        # if nums[-1] != 0:
        #     seq.append((start, end, num_neg))
        # for s, e, n in seq:
        #     if s <= e:
        #         ans = max(ans, get_max(nums[s:e+1], n))
        # return ans
        """
        再来考虑一下DP的解法。首先，这个题和求最大连续子序列和很类似，不同之处在于：1.数组中的0会导致乘积永远为0；2.如果最大乘积为负数，那么
        在后面如果遇到一个负数，可以将其转换为正数。
        根据上述特性，可以设状态方程imax[i]表示以第i个元素结尾的最大乘积，则imax[i]需要更新的情况是：1.imax[i-1]*nums[i]更大（此时nums[i]
        为正数）；2.nums[i]为负数，则此时需要前i-1个元素的最小（负的）乘积，这样乘以一个负数之后会得到更大值；3.当乘积中出现0时或单元素更大的情况
        时，最大值为nums[i]本身。第二种情况目前没有记录，所以需要一个额外的数组记录最小值，设为imin,这个数组记录的是出现的最小乘积（负数）的情况，
        这样在上面的转移方程中可以得到最大值。imin的更新方程同imax。
        此外，imax和imin在每次更新时只需要用到i-1位置的元素，所以可以将空间优化为O(1)使用两个变量记录对应最值。
        """
        imax = [-1e18] * len(nums)
        imin = [1e18] * len(nums)
        imax[0] = imin[0] = nums[0]
        ans = -1e18
        for i in range(1, len(nums)):
            imax[i] = max(nums[i], max(imax[i - 1] * nums[i], imin[i - 1] * nums[i]))
            imin[i] = min(nums[i], min(imax[i - 1] * nums[i], imin[i - 1] * nums[i]))
            ans = max(ans, imax[i])
        return ans


s = Solution()
print(s.maxProduct([-2, 0, -1]))
