#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/28 22:41
# @Author:JiahangGu


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        动态规划法：此前求解过求最长回文子串，状态转移方程为dp[i][j]=dp[i+1][j-1]&&s[i]==s[j]，
        dp[i][j]表示字符串s[i,j]是否为回文子串。且附带特殊情况为
        1.只有一个字符时，比如a是一个回文子串
        2.有两个字符时，如果相等则是回文子串
        3.有三个及以上字符时，如果去掉两边是回文子串且两边字符相等，则是回文子串。
        根据上述条件可知，j-i<2时具有最多两个字符，此时只需要两边相等或只有一个字符即满足回文子
        串，并且也保证了dp[i+1][j-1]不会出现越界的情况
        在求dp[i][j]的时候每出现一个true就表示存在一个回文子串
        时间复杂度O(N2)，空间复杂度O(N2)
        :param s:
        :return:
        """
        # ans = 0
        # n = len(s)
        # dp = [[False] * n for _ in range(n)]
        # for j in range(n):
        #     for i in range(0, j+1):
        #         dp[i][j] = (j - i < 2 or dp[i+1][j-1]) and s[i] == s[j]
        #         if dp[i][j]:
        #             ans += 1
        # return ans
        """
        上述dp方法需要用二维数组记录子串是否是回文的信息，空间复杂度高，可以使用中心扩展的方法，
        以每个字符为中心向两边扩展，如果不是回文就停止转向下一个字符。但需要区分中心字符是一个
        或两个的情况，中心为奇数即一个字符，有n种情况，中心为偶数即两个字符，有n-2种情况，故总
        情况为2n-2种。可以遍历2n-2次，每次声明不同的中心字符串（奇数或偶数）可以一个循环完成
        """
        ans = 0
        n = len(s)
        for i in range(2 * n - 1):
            l = i // 2
            r = i // 2 + i % 2
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        return ans
        """
        Manacher算法
        """
        #TODO


s = Solution()
print(s.countSubstrings("aaa"))
