#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/3 16:24
# @Author:JiahangGu
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        判断课程形成的有向图结构是否含有拓扑排序结构，可以使用DFS或BFS找图中存在的拓扑结构，如果有，那么存在这样
        的排序，返回True。
        之前做过一个求拓扑排序的题，但是掌握不牢固已经遗忘，再做一次希望加深印象
        时间复杂度：假设n为所有课程，m为先修课程限制，则需要首先遍历先修课程得到预处理信息，所需时间O(m)，然后每个
        课程需要遍历一次，所需时间为O(n)，所以总复杂度为O(m+n)
        空间复杂度：同理，需要记录先修课程对应的边为O(m)，同时还要记录所有课程的状态和结果为O(m)，故总复杂度为O(m+n)
        :param numCourses:
        :param prerequisites:
        :return:
        """
        # BFS
        # from collections import defaultdict
        # ans = []
        # edge = defaultdict(list)
        # in_degree = defaultdict(int)
        # for item in prerequisites:
        #     edge[item[1]].append(item[0])
        #     in_degree[item[0]] += 1
        # q = [i for i in range(numCourses) if in_degree[i] == 0]
        # visited = 0
        # while q:
        #     visited += 1
        #     cur_course = q.pop(0)
        #     ans.append(cur_course)
        #     for x in edge[cur_course]:
        #         in_degree[x] -= 1
        #         if in_degree[x] == 0:
        #             q.append(x)
        # return visited == numCourses

        # DFS

        def dfs(node):
            nonlocal cycle_exist
            # nonlocal visited_course
            visited[node] = 1
            for x in edge[node]:
                if visited[x] == 1:
                    cycle_exist = True
                    return
                elif visited[x] == 0:
                    dfs(x)
                    if cycle_exist:
                        return
            visited[node] = 2
            # visited_course += 1

        if not prerequisites:
            return True
        from collections import defaultdict
        # ans = []
        edge = defaultdict(list)
        out_degree = defaultdict(int)
        visited = [0] * numCourses
        cycle_exist = False
        # visited_course = 0
        for item in prerequisites:
            edge[item[1]].append(item[0])
            out_degree[item[1]] += 1
        for i in range(numCourses):
            if visited[i] == 0 and not cycle_exist:
                dfs(i)
        return not cycle_exist


s = Solution()
print(s.canFinish(1, []))
