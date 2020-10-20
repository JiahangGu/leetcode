#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/19 14:41
# @Author:JiahangGu
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """
        s的长度只有100，所以可以使用深搜来检查所有情况下的最小答案。
        每次对当前字符串进行累加或轮转，如果新字符串没有访问过则进入下一层递归。
        :param s:
        :param a:
        :param b:
        :return:
        """
        def add_odd(string, add_num):
            res = ""
            for i in range(len(string)):
                if i & 1:
                    res += str((int(string[i]) + add_num) % 10)
                else:
                    res += string[i]
            return res

        def right_shift(string, shift_num):
            return string[n - shift_num:] + string[:n - shift_num]

        def dfs(string):
            nonlocal ans
            if string in visit:
                return
            ans = min(ans, string)
            visit.add(string)
            add_string = add_odd(string, a)
            if add_string not in visit:
                dfs(add_string)
            shift_string = right_shift(string, b)
            if shift_string not in visit:
                dfs(shift_string)

        n = len(s)
        visit = set()
        ans = s
        dfs(s)
        return ans