#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/28 22:20
# @Author:JiahangGu


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        根据回文字符串的定义可以想到，如果当前字符串是回文，则去掉首尾字符后依然是回文，
        定义dp[i][j]表示字符串[i,j]区间内是否是回文字符，
        则初始化为：dp[i][i]=1
        解的状态为：dp[i][j]==True中最大的j-i，返回对应的子串
        状态转移方程：dp[i][j]=dp[i+1][j-1] and s[i]==s[j]
        需要考虑遍历顺序，由于子串是否回文由更小的子串决定，所以可以按照子串的长度递增序枚举，每种
        长度的子串又有不同的起点，这样可以保证在更新新的子串时所需要的子串的状态已经求出。
        时间复杂度O(N2)，空间复杂度O(N2)
        :param s:
        :return:
        '''
        # n = len(s)
        # dp = [[False]*n for _ in range(n)]
        # for i in range(n):
        #     dp[i][i] = True
        # ans_start, ans_end = -1, -2
        # for length in range(n):
        #     for start in range(n):
        #         end = start + length
        #         if end >= n:
        #             break
        #         elif length == 0:
        #             dp[start][end] = True
        #         elif length == 1:
        #             dp[start][end] = (s[start] == s[end])
        #         else:
        #             dp[start][end] = dp[start+1][end-1] and s[start] == s[end]
        #         if dp[start][end] and end - start > ans_end - ans_start:
        #             ans_end = end
        #             ans_start = start
        # return s[ans_start:ans_end+1]
        '''
        回文子串还可以考虑从中间开始向两边延展判断，如果两边不相等则以该字符为中心没有更大的回文字串。
        需要考虑中心点为单个字符或两个相同字符的情况。
        '''
        ans_start, ans_end = 0, 0
        n = len(s)
        for i in range(1, n):
            offset = 1
            while i + offset < n and i - offset >= 0 and s[i+offset] == s[i-offset]:
                offset += 1
            offset -= 1
            if 2 * offset > ans_end - ans_start:
                ans_end = min(i + offset, n-1)
                ans_start = max(0, i - offset)
        for i in range(1, n):
            if s[i] == s[i-1]:
                offset = 1
                while i + offset < n and i - offset - 1 >= 0 and s[i + offset] == s[i - offset - 1]:
                    offset += 1
                offset -= 1
                if 2 * offset + 2 > ans_end - ans_start:
                    ans_end = min(i + offset, n - 1)
                    ans_start = max(0, i - offset - 1)
        return s[ans_start:ans_end+1]


s = Solution()
x = "cbbd"
print(s.longestPalindrome(x))
