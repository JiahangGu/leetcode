#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/15 9:57
# @Author:JiahangGu
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        大体思路是，首先构造出一个全联通图，然后得到最小生成树。
        :param points:
        :return:
        """
        class Node:
            def __init__(self, x, y, dis):
                self.x = x
                self.y = y
                self.dis = dis

            def __lt__(self, other):
                return self.dis < other.dis

        def find(x):
            if fa[x] == x:
                return x
            else:
                fa[x] = find(fa[x])
                return fa[x]

        def union(x, y):
            fax, fay = find(x), find(y)
            if fax != fay:
                fa[fax] = fay

        import heapq
        edges = []
        fa = [i for i in range(len(points))]
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(edges, Node(i, j, d))
        ans = 0
        cnt_e = 0
        while cnt_e < len(points)-1:
            node = heapq.heappop(edges)
            x, y, dis = node.x, node.y, node.dis
            if find(x) != find(y):
                union(x, y)
                ans += dis
                cnt_e += 1
        return ans
        """
        这里记录使用Prim算法实现的方案。Prim从已有点出发，寻找和MST联通分量相邻的最小权值边。
        """
        # from queue import PriorityQueue as PQ
        # visit = set([i for i in range(len(points))])
        # cal_dis = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        # ans = 0
        # q = PQ()
        # q.put((0, 0))
        # while visit:
        #     weight, pos = q.get()
        #     if pos not in visit:
        #         continue
        #     visit.remove(pos)
        #     ans += weight
        #     for i in visit:
        #         q.put((cal_dis(points[i], points[pos]), i))
        # return ans


s = Solution()
points = [[-8,14],[16,-18],[-19,-13],[-18,19],[20,20],[13,-20],[-15,9],[-4,-8]]
print(s.minCostConnectPoints(points))
