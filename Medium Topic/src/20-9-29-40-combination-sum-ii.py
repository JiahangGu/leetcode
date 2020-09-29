#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/29 10:41
# @Author:JiahangGu
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        由于每个数字只能使用一次，需要在递归时进行去重。去重逻辑如下，首先对数组排序，对于所有连续相同的子数列，首先使用第一个进入下一层递归，
        然后在递归返回后，判断下一个数字是否等于上一个，如果相等，则表示这个数字在此前的递归中已经统计过可行解，也就是i > pos and num[i] = num[i-1]
        以[1,1,1,2,3]为例，首先选择[1]，在[1,1,1]的递归情况返回后，对于第3个1，由于已有[1,1]出现过，此时再统计第3个1就会出现重复解，所以
        应该跳过。
        :param candidates:
        :param target:
        :return:
        """
        def dfs(pos, left, path):
            if left == 0:
                ans.append(path[:])
                return
            if left < 0 or pos >= len(candidates):
                return
            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(i + 1, left - candidates[i], path)
                path.pop()

        candidates.sort()
        ans = []
        dfs(0, target, [])
        return ans
        """
        还有一种解法是，统计每个数字的出现频数，设数字k出现f次，则对于剩余的和left，计算k能放进去的个数，范围在[0, min(f, left // k)]，
        可以统计出k放入0-min(f, left // k)的次数，这个次数不同是肯定不会出现重复解的。在当前递归层结束阶段，要把所有放入的该数字弹出。因为
        最多会放min(f, left // k)次，所以要弹出这么多元素
        """


s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(s.combinationSum2(candidates, target))
