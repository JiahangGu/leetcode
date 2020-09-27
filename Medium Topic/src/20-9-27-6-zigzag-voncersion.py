#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/27 16:08
# @Author:JiahangGu
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        计算当前字符所在行数，使用list的append，在最后按顺序遍历即可
        :param s:
        :param numRows:
        :return:
        """
        if numRows == 1:
            return s
        words = ["" for _ in range(numRows)]
        cur_line = 0
        dir = 1
        for c in s:
            words[cur_line] += c
            cur_line += dir
            if cur_line == numRows - 1:
                dir = -1
            elif cur_line == 0:
                dir = 1
        ans = ""
        for word in words:
            ans += "".join(word)
        return ans


s = Solution()
print(s.convert("LEETCODEISHIRING", 4))
