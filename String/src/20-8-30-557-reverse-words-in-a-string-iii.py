#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/2 21:45
# @Author:JiahangGu


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        翻转单词，开始记录每个空格的位置，计算每个字符在新字符串中的位置
        :param s:
        :return:
        """
        space_pos = [0]
        for i in range(len(s)):
            if s[i] == ' ':
                space_pos.append(i)
        space_pos.append(len(s))
        space_index = 1
        cur_pos = space_pos[space_index] - 1
        ans = [" "] * len(s)
        for i in range(len(s)):
            if s[i] == ' ':
                space_index += 1
                cur_pos = space_pos[space_index] - 1
            else:
                ans[cur_pos] = s[i]
                cur_pos -= 1
        return "".join(ans)


s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
