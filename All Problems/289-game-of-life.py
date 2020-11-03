#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/11/3 15:28
# @Author:JiahangGu
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        模拟即可，统计周围八个细胞的存活个数并根据情况变化，需要注意的是需要复制一个出来，不然无法实现同时的要求。
        """
        # m = len(board)
        # n = len(board[0])
        # cur, pre = [None] * n, [None] * n
        #
        # def get_nei(x, y):
        #     ans = 0
        #     for i in range(-1, 2, 1):
        #         for j in range(-1, 2, 1):
        #             xx = x + i
        #             yy = y + j
        #             if not (xx == x and yy == y) and 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 1:
        #                 ans += 1
        #     return ans
        #
        # for i in range(n):
        #     num = get_nei(0, i)
        #     state = 0
        #     if (board[0][i] == 1 and 2 <= num <= 3) or (board[0][i] == 0 and num == 3):
        #         state = 1
        #     cur[i] = state
        # for i in range(1, m):
        #     pre = cur[:]
        #     for j in range(n):
        #         num = get_nei(i, j)
        #         state = 0
        #         if (board[i][j] == 1 and 2 <= num <= 3) or (board[i][j] == 0 and num == 3):
        #             state = 1
        #         cur[j] = state
        #     board[i - 1] = pre[:]
        # board[m - 1] = cur[:]
        """
        上述方法需要用到额外的O(mn)空间，当数据量大时可能存在问题。并且题目要求in-place修改，可见存在在原数组上直接
        修改的方案。
        需要用到的状态只有死和活，但是由于要求同时变化，所以需要记录单个细胞上一秒的状态，可以做如下定义：
        1.之前为死，现在为死，定义为0
        2.之前为死，现在为活，定义为2,
        3.之前为活，现在为活，定义为1
        4.之前为活，现在为死，定义为-1
        则只需要对数组原地修改，并根据当前状态得知上一秒的状态。最终遍历一次数组将当前-1和2修改为对应状态。
        """
        def get_live_neighbor(x, y, m, n):
            ans = 0
            for dir in neighbors:
                xx = x + dir[0]
                yy = y + dir[1]
                if 0 <= xx < m and 0 <= yy < n and (board[xx][yy] == 1 or board[xx][yy] == -1):
                    ans += 1
            return ans

        m = len(board)
        n = len(board[0])
        neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for i in range(m):
            for j in range(n):
                live = get_live_neighbor(i, j, m, n)
                if board[i][j] == 0:
                    if live == 3:
                        board[i][j] = 2
                else:
                    if live < 2 or live > 3:
                        board[i][j] = -1
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1


s = Solution()
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
s.gameOfLife(board)
print(board)
