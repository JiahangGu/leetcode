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


        # DFS