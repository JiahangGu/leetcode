#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/29 10:03
# @Author:JiahangGu
from typing import List


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        def find(x):
            if x == parent[x]:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]

        parent = [i for i in range(n + 1)]
        for i in range(threshold + 1, n + 1):
            if parent[i] != i:
                continue
            for j in range(i * 2, n + 1, i):
                parent[find(j)] = i

        ans = [find(x) == find(y) for x, y in queries]
        return ans


s = Solution()
n = 6
t = 0
q = [[4,5],[3,4],[3,2],[2,6],[1,3]]
print(s.areConnected(n, t, q))
