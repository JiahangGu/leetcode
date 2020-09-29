#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/29 10:38
# @Author:JiahangGu
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        典型的回溯算法，可以使用一个变量记录当前剩余需要凑的和，每次放入一个数字之后继续递归
        直到剩余和为0记录解，如果小于0则表明非法解结束递归。
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