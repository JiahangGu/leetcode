#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/27 13:12
# @Author:JiahangGu
from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = -1e18
        ans_iter = 0
        queue = 0
        cur_profile = 0
        for i in range(len(customers)):
            if customers[i] + queue <= 4:
                cur_profile += (customers[i] + queue) * boardingCost - runningCost
                queue = 0
            else:
                cur_profile += 4 * boardingCost - runningCost
                queue += customers[i] - 4
            if ans < cur_profile:
                ans_iter = i + 1
                ans = cur_profile
        idx = len(customers) + 1
        while queue > 0:
            cur_profile += min(queue, 4) * boardingCost - runningCost
            if ans < cur_profile:
                ans_iter = idx
                ans = cur_profile
            queue -= 4
            idx += 1
        if ans < 0:
            return -1
        else:
            return ans_iter
