#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/4 9:42
# @Author:JiahangGu
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        本题和207几乎类似，只需要在搜索的时候增加一个记录课程顺序即可。
        留待20-9-07完成，检测拓扑排序的记忆程度
        :param numCourses:
        :param prerequisites:
        :return:
        """
        # BFS
        # from collections import defaultdict
        # edges = defaultdict(list)
        # in_degree = defaultdict(int)
        # for item in prerequisites:
        #     edges[item[1]].append(item[0])
        #     in_degree[item[0]] += 1
        # q = [x for x in range(numCourses) if in_degree[x] == 0]
        # ans = []
        # while q:
        #     cur = q.pop(0)
        #     ans.append(cur)
        #     for x in edges[cur]:
        #         in_degree[x] -= 1
        #         if in_degree[x] == 0:
        #             q.append(x)
        # if len(ans) != numCourses:
        #     return []
        # return ans

        # DFS
        def dfs(cur):
            nonlocal cycle_exist
            visited[cur] = 1
            for x in edges[cur]:
                if visited[x] == 1:
                    cycle_exist = True
                    return
                elif visited[x] == 0:
                    dfs(x)
                    if cycle_exist:
                        return
            ans.append(cur)
            visited[cur] = 2

        from collections import defaultdict
        edges = defaultdict(list)
        out_degree = defaultdict(int)
        for item in prerequisites:
            edges[item[1]].append(item[0])
            out_degree[item[1]] += 1
        visited = [0] * numCourses
        ans = []
        cycle_exist = False
        for i in range(numCourses):
            if visited[i] == 0:
                dfs(0)
        if cycle_exist:
            return []
        return ans[::-1]


s = Solution()
print(s.findOrder(2, [[1,0]]))
