#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/6 14:56
# @Author:JiahangGu
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        BFS和DFS均可做，解题关键是被包围的区间不会存在于边界上，可以想到从边界点的O开始查找所有联通的O，
        并在查找联通分量时标记特殊值。整个完成后，将所有标记特殊值的点标为O，否则为X
        """
        # def dfs(x, y, flag):
        #     if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
        #         return
        #     board[x][y] = flag
        #     for d in dir:
        #         xx = x + d[0]
        #         yy = y + d[1]
        #         dfs(xx, yy, flag)
        #
        # m = len(board)
        # if m == 0:
        #     return
        # n = len(board[0])
        # dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # flag = 'A'
        # for i in range(m):
        #     if board[i][0] == 'O':
        #         dfs(i, 0, flag)
        #     if board[i][n - 1] == 'O':
        #         dfs(i, n - 1, flag)
        # for j in range(n):
        #     if board[0][j] == 'O':
        #         dfs(0, j, flag)
        #     if board[m - 1][j] == 'O':
        #         dfs(m - 1, j, flag)
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] != 'A':
        #             board[i][j] = 'X'
        #         else:
        #             board[i][j] = 'O'
        """
        这里做一下BFS的方法。
        """
        def bfs(x, y, flag):
            q = [(x, y)]
            board[x][y] = flag
            while q:
                cur_x, cur_y = q.pop(0)
                for i in range(4):
                    xx = cur_x + dir[i][0]
                    yy = cur_y + dir[i][1]
                    if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 'O':
                        board[xx][yy] = flag
                        q.append((xx, yy))

        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        flag = 'A'
        for i in range(m):
            if board[i][0] == 'O':
                bfs(i, 0, flag)
            if board[i][n - 1] == 'O':
                bfs(i, n - 1, flag)
        for j in range(n):
            if board[0][j] == 'O':
                bfs(0, j, flag)
            if board[m - 1][j] == 'O':
                bfs(m - 1, j, flag)
        for i in range(m):
            for j in range(n):
                if board[i][j] != 'A':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'
