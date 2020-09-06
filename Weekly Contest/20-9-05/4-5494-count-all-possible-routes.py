#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/5 23:21
# @Author:JiahangGu
from typing import List


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # def dfs(cur_city, left_fuel, path):
        #     nonlocal ans
        #     if left_fuel < 0:
        #         return
        #     if cur_city == finish:
        #         # print(path)
        #         ans = (ans + 1) % (10 ** 9 + 7)
        #     for i in range(0, len(locations)):
        #         if i != cur_city:
        #             path.append(i)
        #             dfs(i, left_fuel - abs(locations[i] - locations[cur_city]), path)
        #             path.pop()
        #
        # ans = 0
        # dfs(start, fuel, [start])
        # return ans
        """
        上述是超时的dfs解法，因为
        :param locations:
        :param start:
        :param finish:
        :param fuel:
        :return:
        """


s = Solution()
print(s.countRoutes([1,2,3], 0, 2, 40))
