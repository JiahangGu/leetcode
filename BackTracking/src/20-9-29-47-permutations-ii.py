#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/29 11:58
# @Author:JiahangGu
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        在普通求排列的解法上，做去重。剪枝条件为，当当前元素已经使用过剪枝，以及当前元素未使用，但和上一个元素值相同，且上一个元素未使用，
        剪枝。对于第二个剪枝情况这里做一下分析，首先和前一个元素相同，就需要做去重，如果前一个元素未使用，则说明当前位置已经填充过前一个元素，
        现在是回溯阶段，因为如果第一次进入递归前一个元素肯定是使用过的，而当前元素已经填充过前一个元素，此时再放入一个相同的元素会产生重复解，
        需要剪枝。
        :param nums:
        :return:
        """
        # def dfs(sol):
        #     if len(sol) == len(nums):
        #         ans.append(sol[:])
        #         return
        #     for i in range(len(nums)):
        #         if flag[i] == 1:
        #             continue
        #         if i > 0 and nums[i] == nums[i - 1] and flag[i - 1] == 0:
        #             continue
        #         flag[i] = 1
        #         dfs(sol + [nums[i]])
        #         flag[i] = 0
        #
        # nums.sort()
        # flag = [0] * len(nums)
        # ans = []
        # dfs([])
        # return ans
        """
        交换的做法也可以实现这一问题。交换的思想是
        """
        def dfs(pos):
            if pos == len(nums):
                ans.append(nums[:])
            flag = set()
            for i in range(pos, len(nums)):
                if nums[i] not in flag:
                    flag.add(nums[i])
                    nums[i], nums[pos] = nums[pos], nums[i]
                    dfs(pos + 1)
                    nums[i], nums[pos] = nums[pos], nums[i]

        ans = []
        dfs(0)
        return ans


s = Solution()
print(s.permuteUnique([1,1,2,2]))
