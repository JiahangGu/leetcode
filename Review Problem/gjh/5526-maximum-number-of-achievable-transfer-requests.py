#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/27 12:47
# @Author:JiahangGu
from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        """
        这道题没做出来的最大原因就是对数据复杂度分析不够深刻。
        提示的数据范围1<=length<=16,2^16也就是2e5的复杂度，是可以接受的。所以这个题的思路应该是
        对于length条边共有2^length-1个组合方式，判断每一种组合方式是否可以保证所有点入度为0
        时间复杂度为O(n*2^n)，n<=16可行。
        :param n:
        :param requests:
        :return:
        """
        ans = 0
        length = len(requests)
        max_iter = (1 << length)
        for i in range(1, max_iter):
            degree = [0] * n
            j = 0
            k = 1
            cnt = 0
            while j < length:
                # 选择第j条边
                if i & k:
                    degree[requests[j][1]] += 1
                    degree[requests[j][0]] -= 1
                    cnt += 1
                k <<= 1
                j += 1
            flag = True
            for j in range(n):
                if degree[j]:
                    flag = False
                    break
            if flag:
                ans = max(ans, cnt)
        return ans


s = Solution()
n = 3
requests = [[0,0],[1,2],[2,1]]
print(s.maximumRequests(n, requests))
