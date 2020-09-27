#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/3 11:37
# @Author:JiahangGu
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        相比n皇后普通版的多了一个记录解法的条件，所以在普通版的基础上新增path记录每个点的纵坐标，在达到最后一行
        可行解之后，构造解并记录。皇后的攻击范围为同行同列同对角线，由于同行不可能出现（向下递归），所以判断同列
        和对角线即可。
        时间复杂度为O(n!)，空间复杂度为O(n)，需要记录当前方案的纵坐标，而每个数字的索引就是对应的横坐标。
        :param n:
        :return:
        """
        def construct_answer(coordinate):
            grid = [["."] * n for _ in range(n)]
            for i in range(len(coordinate)):
                grid[i][coordinate[i]] = 'Q'
            res = []
            for row in grid:
                res.append("".join(row))
            ans.append(res)

        def dfs(k, path):
            if k >= n:
                construct_answer(path)
            for col in range(n):
                flag = True
                for row in range(len(path)):
                    if col == path[row] or k + path[row] == row + col or k + col == path[row] + row:
                        flag = False
                        break
                if flag:
                    path.append(col)
                    dfs(k+1, path)
                    path.pop()

        ans = []
        path = []
        dfs(0, path)
        return ans


s = Solution()
# print(s.solveNQueens(4))
ans = s.solveNQueens(8)
print(len(ans))
# for row in ans:
#     for col in row:
#         print(col)
#     print("")
