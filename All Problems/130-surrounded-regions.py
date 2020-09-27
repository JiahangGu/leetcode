#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/4 15:50
# @Author:JiahangGu
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        首先使用搜索找出所有被分离的联通区域，并对同一个联通块标号。然后遍历边界找出在边界的0点，并且记录
        对应标号，则这些标号都不会修改为X，那么剩余的区域的O都要修改为X。
        :param board:
        :return:
        """
        def dfs(x, y, flag):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
                return
            board[x][y] = flag
            for d in dir:
                xx = x + d[0]
                yy = y + d[1]
                dfs(xx, yy, flag)

        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        flag = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    dfs(i, j, str(flag))
                    flag += 1
        from collections import defaultdict
        region = defaultdict(bool)
        for i in range(n):
            if board[0][i] != 'X':
                region[board[0][i]] = True
            if board[m-1][i] != 'X':
                region[board[m-1][i]] = True
        for i in range(m):
            if board[i][0] != 'X':
                region[board[i][0]] = True
            if board[i][n-1] != 'X':
                region[board[i][n-1]] = True
        for i in range(m):
            for j in range(n):
                if board[i][j] != 'X':
                    if not region[board[i][j]]:
                        board[i][j] = 'X'
                    else:
                        board[i][j] = 'O'
        """
        参考官方题解，本题可以直接从边界的O开始搜索，所有与边界的O联通的点都无视，而在区域内被包围的则变为X。
        而使用dfs和bfs的方式一样，bfs首先要记录边界点中需要开始的点即O点放入队列中，当栈非空时取出该点，求所有
        满足条件的邻点即O，并标记为特殊字符，在最终遍历完成后修改特殊字符为目标字符。
        """


s = Solution()
board = [["X","O","X","X"]]
s.solve(board)
print(board)
