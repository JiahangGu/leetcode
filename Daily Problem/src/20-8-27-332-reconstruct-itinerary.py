#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/27 10:35
# @Author:JiahangGu

from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        由于至少存在一种合理的行程，所以只需要按照在每个节点选择字典序最小的站点，如果能到达解状态则是最小的解，如果不能
        则继续回溯寻找解。
        最终结束状态应该为len(ans)=len(tickets)+1
        此外需要注意的点是记录path之后要删除对应边，防止进入深层递归二次查询。如果当前站点没有邻接点，可以提前结束，当前
        path不可能是解（进入了死胡同）。如果遍历完所有邻接点都没有找到解，那当前path也不可能是解，返回false。
        :param tickets:
        :return:
        """
        # def _dfs(path, cur_pos, pos_dict, tickets_num):
        #     if len(path) == tickets_num + 1:
        #         return True
        #     if len(pos_dict[cur_pos]) == 0:
        #         return False
        #     for i in range(len(pos_dict[cur_pos])):
        #         cur_to = pos_dict[cur_pos].pop(i)
        #         path.append(cur_to)
        #         if _dfs(path, cur_to, pos_dict, tickets_num):
        #             return True
        #         path.pop()
        #         pos_dict[cur_pos].insert(i, cur_to)
        #     return False
        #
        # tickets_num = len(tickets)
        # pos_dict = defaultdict(list)
        # for f, t in tickets:
        #     pos_dict[f].append(t)
        # for k, v in pos_dict.items():
        #     v.sort()
        # path = ["JFK"]
        # _dfs(path, "JFK", pos_dict, tickets_num)
        # return path
        """
        欧拉图解法。已知存在解，则题目转换为找到机场图的一条欧拉路径。根据点的入度出度可知，如果相差1，则进入该点
        后为死路，无法进入后续点。所以在死胡同时用栈记录该点即可得到行程顺序。而进入非死胡同的点，只需继续向深度递
        归，直到死胡同记录点后回溯，即可得到行程的逆序。
        所以递归策略为，如果当前点为死胡同，记录该点，回溯，如果当前点具有邻接点，递归。并且由于要按照最小的字典序输出结果
        应该先对所有邻接点排序，每次访问完之后删除已访问的节点和边。
        """
        def _dfs(cur_pos):
            while pos_dict[cur_pos]:
                pos = pos_dict[cur_pos].pop(0)
                _dfs(pos)
            path.append(cur_pos)

        pos_dict = defaultdict(list)
        for f, t in tickets:
            pos_dict[f].append(t)
        for k, v in pos_dict.items():
            v.sort()
        path = []
        _dfs("JFK")
        return path[::-1]


x = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
s = Solution()
ans = s.findItinerary(x)
print(ans)
print(len(ans))
print(len(x))