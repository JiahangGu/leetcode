#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/9 9:28
# @Author:JiahangGu
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        回溯法，可以设定一个剩余的值k，k==0时保存当前解，k>0继续递归,k<0时结束。
        这里需要注意重复解的问题：比如要拼凑一个6，如果存在[2,4]则在2时会选择4，而在4时要避免选择2.
        首先对candidates排序，因为保证元素不重复出现，只要保证递归顺序时升序即可，这样在当前数只能向后
        选择，而在他之前如果可以拼凑成可行解则已经统计过。
        :param candidates:
        :param target:
        :return:
        """
        def back_track(cur_pos, k, path):
            if k == 0:
                ans.append(path[:])
                return
            if k < 0 or cur_pos >= len(candidates):
                return
            for i in range(cur_pos, len(candidates)):
                path.append(candidates[i])
                back_track(i, k-candidates[i], path)
                path.pop()

        ans = []
        candidates.sort()
        back_track(0, target, [])
        return ans


s = Solution()
candidates = [2, 3, 5]
target = 8
print(s.combinationSum(candidates, target))
