#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/20 10:20
# @Author:JiahangGu
from typing import List


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        """
        根据结点个数n<1000基本可以排除n^2算法，所以使用gcd的方法肯定不行。
        对于查询两点是否属于同一集合（或是否连通）的问题最好的方法是并查集，因为并查集的时间复杂度通过摊还分析可以
        得出是O(1)。
        可以得知，i,i*2,i*3...i*k是连通的，则遍历i，并将i的所有倍数和i连通。
        并且可以根据parent[i]判断i是否已处理。
        :param n:
        :param threshold:
        :param queries:
        :return:
        """
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