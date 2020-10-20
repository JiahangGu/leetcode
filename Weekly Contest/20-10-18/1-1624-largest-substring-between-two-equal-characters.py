#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/19 14:39
# @Author:JiahangGu
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        记录每个字符最后一次出现的位置，在遇到出现过的字符后计算距离
        :param s:
        :return:
        """
        dic = dict()
        ans = -1
        for i in range(len(s)):
            if s[i] in dic:
                ans = max(ans, i - dic[s[i]] - 1)
            else:
                dic[s[i]] = i
        return ans
