#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/4 15:50
# @Author:JiahangGu
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        首先使用搜索找出所有被分离的联通区域，并使用并查集算法标号。然后遍历边界找出在边界的0点，并且记录
        对应标号，则这些标号都不会修改为X，那么剩余的区域的O都要修改为X。
        :param board:
        :return:
        """
        def find(x):
