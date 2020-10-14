#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/14 15:20
# @Author:JiahangGu
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        首先一次遍历得到所有单词（碰到空格就保存当前单词）和单词对应的长度，第二次遍历进行翻转，首先根据长度得到单词的起点
        和终点，做拼接。思路清晰，不再实现，使用python简单实现一下。
        :param s:
        :return:
        """
        words = []
        word = ""
        for c in s:
            if c == ' ':
                if word:
                    words.append(word)
                word = ""
            else:
                word += c
        if word:
            words.append(word)
        return " ".join(words[::-1])


s = Solution()
ss = "  Bob    Loves  Alice   "
print(s.reverseWords(ss))
