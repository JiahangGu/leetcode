#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/30 13:57
# @Author:JiahangGu
from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        """
        解题思路：岛屿对应图中标为1的连通分量，如果个数为0或大于1，则表示岛屿已分离，如果为1则表示未分离，需要找到连接
        两个岛屿的单个陆地变为水。
        一个关键点是，一张图最多两天一定能出现分离的岛屿，因为必有点只与最多两个陆地单元相邻，（如果陆地在边界则边界想象
        成水），那么修改这两个相邻的陆地则岛屿已分离。
        方法：判断岛是否分离，如果不分离，判断是否可以修改一个陆地单元达到分离，如果可以则1天，不然则2天，最多2天。
        这道题没做出来的主要原因是卡在了最多2天这里，没有考虑清楚划分岛屿的技巧（即存在一个陆地单元最多与2个陆地相邻），
        其实可以直接考虑全是陆地的情况，这一定是最特殊的。
        :param grid:
        :return:
        """
        import copy

        def is_connected(row, col):
            def dfs(x, y, color):
                if x < 0 or x >= row or y < 0 or y >= col or tmp[x][y] == color or tmp[x][y] == 0:
                    return
                tmp[x][y] = color
                dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
                for dir_x, dir_y in dirs:
                    xx = x + dir_x
                    yy = y + dir_y
                    dfs(xx, yy, color)

            connect_num = 4
            tmp = copy.deepcopy(grid)
            for i in range(row):
                for j in range(col):
                    if tmp[i][j] == 1:
                        connect_num += 1
                        dfs(i, j, connect_num)
            if connect_num > 5 or connect_num == 4:
                return True
            return False

        row = len(grid)
        col = len(grid[0])
        if is_connected(row, col):
            return 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if is_connected(row, col):
                        return 1
                    grid[i][j] = 1
        return 2


s = Solution()
print(s.minDays([[0,1,1,0],[0,1,1,0],[0,0,0,0]]))
