#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/16 22:38
# @Author:JiahangGu
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        染色法判断二分图，从任一未染色节点开始，染色，遍历邻点，如果邻点未染色，染成不同
        色，继续，如果染色且和该点同色，不是二分图，否则继续遍历。
        DFS解法
        :param graph:
        :return:
        '''
        col = [0] * len(graph)

        def dfs(i, color):
            col[i] = color
            for j in graph[i]:
                if col[j] == 0 and not dfs(j, -color):
                    return False
                elif col[j] == color:
                    return False
            return True

        for i in range(len(graph)):
            if col[i] == 0:
                if not dfs(i, 1):
                    return False
        return True


s = Solution()
x = [[1,2,3], [0,2], [0,1,3], [0,2]]
print(s.isBipartite(x))
