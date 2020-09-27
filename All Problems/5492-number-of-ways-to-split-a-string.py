#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/5 22:49
# @Author:JiahangGu


class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        cnt1 = 0
        pos = []
        for i in range(n):
            if s[i] == '1':
                cnt1 += 1
                pos.append(i)
        if cnt1 % 3 != 0:
            return 0
        MOD = 10 ** 9 + 7
        if cnt1 == 0:
            return (n-1) * (n-2) // 2 % MOD
        x = cnt1 // 3
        pos1 = pos[x-1]
        pos2 = pos[x]
        pos3 = pos[2*x - 1]
        pos4 = pos[2*x]
        left0 = pos2 - pos1 - 1
        right0 = pos4 - pos3 - 1
        return ((left0+1) % MOD) * ((right0+1) % MOD) % MOD


s = Solution()
print(s.numWays("100100010100110"))
