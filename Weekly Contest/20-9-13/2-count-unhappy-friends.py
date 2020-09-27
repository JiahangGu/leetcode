#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/15 9:38
# @Author:JiahangGu
from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """
        记录亲近程度，遍历pairs，使用集合存储不开心的所有人，注意这里同一个人可能匹配到不同的队友都会
        不开心，可能存在重复记录。
        :param n:
        :param preferences:
        :param pairs:
        :return:
        """
        def is_unhappy(x, y, u, v):
            if pref[x][u] > pref[x][y] and pref[u][x] > pref[u][v]:
                return True
            return False

        from collections import defaultdict
        pref = defaultdict(dict)
        unhappy = set()
        for i in range(len(preferences)):
            for j in range(len(preferences[i])):
                pref[i][preferences[i][j]] = n - j
        for i in range(len(pairs)-1):
            x, y = pairs[i][0], pairs[i][1]
            for j in range(i+1, len(pairs)):
                u, v = pairs[j][0], pairs[j][1]
                if is_unhappy(x, y, u, v):
                    unhappy.add(x)
                if is_unhappy(y, x, u, v):
                    unhappy.add(y)
                if is_unhappy(x, y, v, u):
                    unhappy.add(x)
                if is_unhappy(y, x, v, u):
                    unhappy.add(y)
                if is_unhappy(u, v, x, y):
                    unhappy.add(u)
                if is_unhappy(v, u, x, y):
                    unhappy.add(v)
                if is_unhappy(u, v, y, x):
                    unhappy.add(u)
                if is_unhappy(v, u, y, x):
                    unhappy.add(v)
        return len(unhappy)


s = Solution()
n = 4
preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
pairs = [[1, 3], [0, 2]]
print(s.unhappyFriends(n, preferences, pairs))
