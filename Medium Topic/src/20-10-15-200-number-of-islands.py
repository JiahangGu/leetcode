#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/15 17:35
# @Author:JiahangGu
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        使用DFS或BFS找到从一个未标记的陆地点开始的联通分量并标记。遍历完所有的点之后即可得到存在多少个这样的连通分量。
        :param grid:
        :return:
        """
        # def bfs(x, y, flag):
        #     dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        #     queue = [(x, y)]
        #     grid[x][y] = flag
        #     while queue:
        #         xx, yy = queue.pop(0)
        #         for i in range(4):
        #             tmp_x, tmp_y = xx + dirs[i][0], yy + dirs[i][1]
        #             if 0 <= tmp_x < m and 0 <= tmp_y < n and grid[tmp_x][tmp_y] == '1':
        #                 queue.append((tmp_x, tmp_y))
        #                 grid[tmp_x][tmp_y] = flag
        #
        # ans = 2
        # m = len(grid)
        # n = len(grid[0])
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '1':
        #             bfs(i, j, ans)
        #             ans += 1
        # return ans - 2
        """
        搜索没有什么难度，这里使用并查集来解决这个问题。并查集解决问题的关键在于对所有相连的陆地进行连接(union)操作。
        这里需要注意的是：1.所有水域都不需要连接，或者连接到一个虚拟的结点。2.遍历时保持一个方向即可，即向右向下（习惯），
        因为union是互相的，保持一个即可。
        主要是熟悉一下对并查集的使用。
        """
        class UnionSet:
            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for _ in range(n)]

            def find(self, r):
                while self.parent[r] != r:
                    self.parent[r] = self.parent[self.parent[r]]
                    r = self.parent[r]
                return r

            def is_connected(self, p, q):
                return self.find(p) == self.find(q)

            def union(self, p, q):
                p = self.find(p)
                q = self.find(q)
                if p == q:
                    return
                if self.rank[p] < self.rank[q]:
                    self.parent[p] = q
                elif self.rank[q] < self.rank[p]:
                    self.parent[q] = p
                else:
                    self.parent[p] = q
                    self.rank[q] += 1
                self.count -= 1

        def get_index(i, j):
            return i * n + j

        m = len(grid)
        n = len(grid[0])
        dirs = [[1, 0], [0, 1]]
        dump = m * n
        us = UnionSet(m * n + 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for dir in dirs:
                        x = i + dir[0]
                        y = j + dir[1]
                        if x < m and y < n and grid[x][y] == '1':
                            us.union(get_index(x, y), get_index(i, j))
                else:
                    us.union(get_index(i, j), dump)
        return us.count - 1


s = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(s.numIslands(grid))
