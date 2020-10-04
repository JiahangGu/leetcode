#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/29 11:34
# @Author:JiahangGu
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        全排列解法模板，逐层替换。例如[1,2,3]，则生成顺序为[1,2,3],然后互换23得到[1,3,2]，然后递归结束，互换12得到[2,1,3]，
        然后互换13得到[2,3,1]，递归结束互换13得到[3,2,1]，互换21得到[3,1,2]
        :param nums:
        :return:
        """
        # def dfs(pos):
        #     if pos == len(nums):
        #         ans.append(nums[:])
        #     for i in range(pos, len(nums)):
        #         nums[i], nums[pos] = nums[pos], nums[i]
        #         dfs(pos + 1)
        #         nums[i], nums[pos] = nums[pos], nums[i]
        #
        # ans = []
        # dfs(0)
        # return ans
        """
        方案2，使用标记数组记录已使用的数字。
        """
        def dfs(sol):
            if len(sol) == len(nums):
                ans.append(sol[:])
                return
            for i in range(len(nums)):
                if flag[i] == 0:
                    flag[i] = 1
                    dfs(sol + [nums[i]])
                    flag[i] = 0

        flag = [0] * len(nums)
        ans = []
        dfs([])
        return ans


s = Solution()
print(s.permute([1,2,3]))