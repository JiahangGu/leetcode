#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 21:14
# @Author:JiahangGu
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        首先考虑不包含重复元素的解法。从空集合开始，每次进入深层递归都应该将当前解放入解空间中。直到遍历完成。
        现在考虑去重操作，首先排序（去重剪枝都需要排序），如果当前元素和前一个元素相等且不是第一个，跳过。
        比如[1,2,2]，对于第1个2来说，已经得到了[1,2],[1,2,2]的解，那么第2个2对应的解[1,2]就是重复的，这里
        判断第一位的方式是使用标记数组，如果前一位没有使用，那就是回溯回来的，这样的情况是重复解，所以跳过。
        :param nums:
        :return:
        """
        def dfs(path, pos):
            ans.append(path[:])
            if pos == len(nums):
                return
            for i in range(pos, len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not flag[i - 1]:
                    continue
                flag[i] = True
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()
                flag[i] = False

        flag = [False] * len(nums)
        nums.sort()
        ans = []
        dfs([], 0)
        return ans


s = Solution()
print(s.subsetsWithDup([1,2,2]))
