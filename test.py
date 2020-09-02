#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/29 10:03
# @Author:JiahangGu


class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
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
print(s.minDays([[1,1]]))