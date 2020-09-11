#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/28 22:41
# @Author:JiahangGu
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        扫雷游戏，大意就是分为三种情况
        1.如果挖到了雷结束（只需要修改雷）
        2.一个没有相邻地雷的空块被挖出，改为B，并递归揭露所有相邻的方块
        3.至少与一个雷相邻的空块被挖出，修改他为相邻雷数量
        分析完之后具体思路可以大致确定，首先需要一个确定相邻雷的函数get_mines，其后从初始点开始搜索（判断该点应该改为怎样的符号）
        ，如果遇到相邻点是空白方块，对方块进行搜索，进行后续搜索。
        注意这里题目中说明了相邻的含义是上下左右和对角线，而之前有一次没通过的提交是认为求雷是这样，而连接的块是只有上下左右，所以失败了。
        DFS解法就不再说明，思路一样。
        :param board:
        :param click:
        :return:
        """
        def get_mines(x, y):
            ans = 0
            for item in dirs:
                xx = x + item[0]
                yy = y + item[1]
                if 0 <= xx < m and 0 <= yy < n and (board[xx][yy] == 'M' or board[xx][yy] == 'X'):
                    ans += 1
            return ans

        m = len(board)
        n = len(board[0])
        # ans = [[]]
        # in-place
        q = [click]
        flag = [[False] * n for _ in range(m)]
        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        flag[click[0]][click[1]] = True
        while q:
            item = q.pop(0)
            x, y = item[0], item[1]
            if board[x][y] == 'M':
                board[x][y] = 'X'
            elif board[x][y] == 'E' or board[x][y] == 'e':
                mines = get_mines(x, y)
                if mines != 0:
                    board[x][y] = str(mines)
                else:
                    board[x][y] = 'B'
                    for dir in dirs:
                        xx = x + dir[0]
                        yy = y + dir[1]
                        if 0 <= xx < m and 0 <= yy < n and (board[xx][yy] == 'M' or board[xx][yy] == 'E') and not flag[xx][yy]:
                            q.append([xx, yy])
                            flag[xx][yy] = True
            else:
                continue
        return board


s = Solution()
board = [["E","E","E","E","E","E","E","E"],
         ["E","E","E","E","E","E","E","M"],
         ["E","E","M","E","E","E","E","E"],
         ["M","E","E","E","E","E","E","E"],
         ["E","E","E","E","E","E","E","E"],
         ["E","E","E","E","E","E","E","E"],
         ["E","E","E","E","E","E","E","E"],
         ["E","E","M","M","E","E","E","E"]]
click = [0, 0]
# print(s.updateBoard(board, click))
ans = s.updateBoard(board, click)
for item in ans:
    print(item)
