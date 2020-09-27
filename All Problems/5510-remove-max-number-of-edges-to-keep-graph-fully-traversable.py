#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/6 11:08
# @Author:JiahangGu
from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # def bfs(start, edge_flag, visit):
        #     visit_num = 0
        #     q = [start]
        #     while q:
        #         node = q.pop(0)
        #         visit[node] = True
        #         visit_num += 1
        #         for v in edge3[node]:
        #             if not visit[v]:
        #                 q.append(v)
        #                 visit[v] = True
        #         for v in edge_flag[node]:
        #             if not visit[v]:
        #                 q.append(v)
        #                 visit[v] = True
        #     return visit_num >= n
        #
        # def cycle_exist(start, edge_flag, in_degree):
        #     q = [start]
        #     visit_nodes = 0
        #     while q:
        #         node = q.pop(0)
        #         visit_nodes += 1
        #         for v in edge_flag[node]:
        #             in_degree[v] -= 1
        #             edge_flag[node].remove(v)
        #             if in_degree[v] == 0:
        #                 q.append(v)
        #         for v in edge3_temp[node]:
        #             in_degree[v] -= 1
        #             edge3_temp[node].remove(v)
        #             if in_degree[v] == 0:
        #                 q.append(v)
        #     return visit_nodes != n
        #
        # from collections import defaultdict
        # edge3 = defaultdict(list)
        # edge2 = defaultdict(list)
        # edge1 = defaultdict(list)
        # in_degree1 = defaultdict(int)
        # in_degree2 = defaultdict(int)
        # for t, u, v in edges:
        #     if t == 3:
        #         edge3[u].append(v)
        #         in_degree1[u] += 1
        #         in_degree2[u] += 1
        #     elif t == 2:
        #         edge2[u].append(v)
        #         in_degree2[u] += 1
        #     elif t == 1:
        #         edge1[u].append(v)
        #         in_degree1[u] += 1
        # ans = 0
        # # 存在有3的重复边则删除12
        # for k, v in edge3.items():
        #     for node in v:
        #         if edge2.get(k, None) and node in edge2.get(k):
        #             edge2.get(k).remove(node)
        #             in_degree2[k] -= 1
        #             ans += 1
        #         if edge1.get(k, None) and node in edge1.get(k):
        #             edge1.get(k).remove(node)
        #             in_degree1[k] -= 1
        #             ans += 1
        #
        # visit_alice = [False] * (n + 1)
        # visit_bob = [False] * (n + 1)
        # alice_traverse = bfs(edges[0][1], edge1, visit_alice)
        # bob_traverse = bfs(edges[0][1], edge2, visit_bob)
        # if not alice_traverse or not bob_traverse:
        #     return -1
        # # 找出alice和bob遍历路径中的所有环
        # from copy import deepcopy
        # while True:
        #     in_degree = deepcopy(in_degree1)
        #     edge_flag = deepcopy(edge1)
        #     edge3_temp = deepcopy(edge3)
        #     if cycle_exist(edges[0][1], edge_flag, in_degree):
        #         ans += 1
        #         if len(edge_flag.items()) > 0:
        #             for k, v in edge_flag.items():
        #                 edge1[k].remove(v)
        #                 in_degree1[v] -= 1
        #                 break
        #         elif len(edge3_temp.items()) > 0:
        #             for k, v in edge3_temp.items():
        #                 edge3[k].remove(v)
        #                 in_degree1[v] -= 1
        #     else:
        #         break
        # while True:
        #     in_degree = deepcopy(in_degree2)
        #     edge_flag = deepcopy(edge2)
        #     edge3_temp = deepcopy(edge3)
        #     if cycle_exist(edges[0][1], edge_flag, in_degree):
        #         ans += 1
        #         if len(edge_flag.items()) > 0:
        #             for k, v in edge_flag.items():
        #                 edge2[k].remove(v)
        #                 in_degree2[v] -= 1
        #                 break
        #         elif len(edge3_temp.items()) > 0:
        #             for k, v in edge3_temp.items():
        #                 edge3[k].remove(v)
        #                 in_degree2[v] -= 1
        #     else:
        #         break
        # return ans
        """
        上述解法是比赛中想到的，思路是这样：
        1.做一次遍历查询alice和bob是否能走到所有点，即是否连通，如果不是返回-1
        2.扫描123类型的边，并且如果存在和3类型重复的边可直接删除
        3.当alice和bob的连通图中存在环时，删除一条环中的边，直到不存在环，则这时的图一定时联通的并且是最少的边
        但是在删除环的算法中存在一些问题：1是复杂度高，要遍历到没有环为止；2是环中的边不好确定，要入度>0并且还要
        找到对应的边。
        比赛结束后，参考题解发现不需要计算去掉边的个数，而是记录可用边（这里的可用边指的是不参与环的边)，并且要求
        alice和bob均可遍历，则需要使用2*n-2条边，其中要减去类型为3且不在环里的边，因为3只需要一条。这样只需要
        求出3构成的图中不构成环的最大边数，最终答案为len(edges)-(2*n-2)-类型3的不构成的环的边数
        :param n:
        :param edges:
        :return:
        """
        from collections import defaultdict
        edge1 = defaultdict(set)
        edge2 = defaultdict(set)
        edge3 = defaultdict(set)

        for t, u, v in edges:
            if t == 1:
                edge1[u].add(v)
                edge1[v].add(u)
            elif t == 2:
                edge2[u].add(v)
                edge2[v].add(u)
            elif t == 3:
                edge1[u].add(v)
                edge1[v].add(u)
                edge2[u].add(v)
                edge2[v].add(u)
                edge3[u].add(v)
                edge3[v].add(u)
        visited = [False] * n
        count = 0

        def dfs(start, edge):
            nonlocal count
            if visited[start-1]:
                return
            visited[start-1] = True
            for x in edge[start]:
                if not visited[x-1]:
                    count += 1
                    dfs(x, edge)

        for i in edge3:
            dfs(i, edge3)
        num3 = count

        visited = [False] * n
        dfs(1, edge1)
        if not all(visited):
            return -1

        visited = [False] * n
        dfs(1, edge2)
        if not all(visited):
            return -1
        return len(edges) - (2 * n - 2 - num3)


s = Solution()
edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
print(s.maxNumEdgesToRemove(4, edges))
