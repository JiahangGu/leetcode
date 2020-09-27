#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/14 9:21
# @Author:JiahangGu
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        dfs搜索即可，设定一个flag数组标记是否使用过。
        :param board:
        :param word:
        :return:
        """
        def dfs(target, x, y):
            if not target:
                return True
            if not 0 <= x < m or not 0 <= y < n or flag[x][y]:
                return False
            if board[x][y] != target[0]:
                return False
            flag[x][y] = True
            for dir in dirs:
                xx, yy = x + dir[0], y + dir[1]
                if dfs(target[1:], xx, yy):
                    return True
            flag[x][y] = False

        m = len(board)
        n = len(board[0])
        flag = [[False] * n for _ in range(m)]
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in range(m):
            for j in range(n):
                if dfs(word, i, j):
                    return True
        return False


s = Solution()
board =[
  "a"
]
word = "a"
print(s.exist(board, word))
