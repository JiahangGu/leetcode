#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/15 15:11
# @Author:JiahangGu
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        回溯法，每次添加一个数字要判断是否会和已存在的数字冲突，判断冲突可以使用hash做，存储每一行、每一列以及每一个
        3*3宫格内出现过的数字，如果该位置加入的数字满足数独的条件则继续递归。最终填满所有格子且不产生冲突则有解。
        注意在实现过程中涉及到遍历问题，由于给定只有81个格子，且只有部分格子要填，所以可以记录下所有需要填数字的格子，
        如果所有格子均可以填数字则得到解
        :param board:
        :return:
        """
        def dfs(pos):
            if pos == len(space):
                return True
            x, y = space[pos]
            for i in range(9):
                if not hash_row[x][i] and not hash_col[y][i] and not hash_square[x // 3 * 3 + y // 3][i]:
                    hash_row[x][i] = True
                    hash_col[y][i] = True
                    hash_square[x // 3 * 3 + y // 3][i] = True
                    board[x][y] = str(i+1)
                    if dfs(pos+1):
                        return True
                    board[x][y] = '.'
                    hash_row[x][i] = False
                    hash_col[y][i] = False
                    hash_square[x // 3 * 3 + y // 3][i] = False
            return False

        hash_row = [[False for _ in range(9)] for _ in range(9)]
        hash_col = [[False for _ in range(9)] for _ in range(9)]
        hash_square = [[False for _ in range(9)] for _ in range(9)]
        space = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    hash_row[i][int(board[i][j])-1] = True
                    hash_col[j][int(board[i][j])-1] = True
                    hash_square[i // 3 * 3 + j // 3][int(board[i][j])-1] = True
                else:
                    space.append((i, j))
        dfs(0)


s = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)
for x in board:
    print(x)
