#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/28 17:37
# @Author:JiahangGu

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        暴力法：比较长度为2-length/2的子串是否重复出现。时间复杂度：设n为长度，则遍历到长度i时，内层循环遍历
        n//i，总遍历次数为n//2+n//3+...+1，求和的结果为nlnn+Cn，是个近似值
        :param s:
        :return:
        """
        # for i in range(1, len(s)//2+1):
        #     cur = 0
        #     while cur+i+i <= len(s) and s[cur:cur+i] == s[cur+i:cur+i+i]:
        #         cur += i
        #     if cur+i == len(s):
        #         return True
        # return False
        """
        字符串匹配的方法：如果该字符可以划分为若干个重复出现的子串，那如果将该字符串拼接在后面，并去掉重复的一个字串，
        原字符串仍是新字符串的子串，所以可以将两个字符串连在一起，然后移除第一个字符和最后一个字符，如果s仍是新字符串
        的子串那么s满足题目要求，证明见官方题解。在实现方面，可以使用find函数，如果在新字符串找到s则s满足题意
        """
        # new_s = (s+s)
        # return new_s[1:-1].find(s) != -1
        """
        KMP算法。KMP算法介绍见../String/字符串匹配.doc。
        """
        def get_next(pattern):
            i = -1
            j = 0
            next = [-1] * len(pattern)
            while j < len(pattern)-1:
                if i == -1 or pattern[i] == pattern[j]:
                    i += 1
                    j += 1
                    if pattern[i] != pattern[j]:
                        next[j] = i
                    else:
                        next[j] = next[i]
                else:
                    i = next[i]
            return next

        def kmp(target, pattern):
            next = get_next(pattern)
            i, j = 0, 0
            while i < len(target) and j < len(pattern):
                if j == -1 or pattern[j] == target[i]:
                    i += 1
                    j += 1
                else:
                    j = next[j]
            if j >= len(pattern):
                return i - len(pattern)
            return -1
        target = (s + s)[1:-1]
        start_pos = kmp(target, s)
        if start_pos != len(s) and start_pos != -1:
            return True
        return False


s = Solution()
print(s.repeatedSubstringPattern("aba"))
