#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/16 11:52
# @Author:JiahangGu
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        判断图中是否存在环，使用拓扑排序判断。BFS方法求解拓扑排序时，每次在弹出队首元素后，
        将所有邻点的结点入度-1，并将入度为0的结点放入队列中。弹出队列的元素顺序就是拓扑序。如果结点个数
        少于n，则存在环（循环提前终止）。
        :param numCourses:
        :param prerequisites:
        :return:
        """
        # from collections import defaultdict
        # edges = defaultdict(list)
        # degree = defaultdict(int)
        # for t, f in prerequisites:
        #     edges[f].append(t)
        #     degree[t] += 1
        # queue = [i for i in range(numCourses) if degree[i] == 0]
        # count = 0
        # while queue:
        #     cur = queue.pop(0)
        #     count += 1
        #     for x in edges[cur]:
        #         degree[x] -= 1
        #         if degree[x] == 0:
        #             queue.append(x)
        # return count == numCourses
        """
        DFS解法。由于DFS会从一个起点开始遍历到无法继续前进才停止，所以更重要的是结点的出度。当出度为0时就不再深搜。同时为了避免陷入环，
        需要使用一个状态数组标记结点的访问状态。如果待访问结点正在被访问，则说明存在环。如果未被访问，则继续递归搜索。如果已被访问则跳过。
        """
        def dfs(pos):
            nonlocal flag
            visit[pos] = 1
            for x in edges[pos]:
                if visit[x] == 1:
                    flag = False
                    return
                elif visit[x] == 0:
                    dfs(x)
                    if not flag:
                        return
            visit[pos] = 2

        flag = True
        visit = [0] * numCourses
        from collections import defaultdict
        edges = defaultdict(list)
        degree = defaultdict(int)
        for t, f in prerequisites:
            edges[f].append(t)
            degree[f] += 1
        for i in range(numCourses):
            if flag and visit[i] == 0:
                dfs(i)
        return flag


s = Solution()
print(s.canFinish(2, [[1,0],[0,1]]))
