#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/28 10:17
# @Author:JiahangGu
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        有效括号需要满足的条件为在第i位，左括号的数量必须大于等于右括号。所以可以使用回溯算法，记录当前可用的左括号和右括号数量，
        如果当前可以放右括号（左括号个数大于右括号），放右括号，进入下一层递归。如果左括号还有剩余，放左括号，进入下一层递归。
        需要记录当前左右括号的个数。
        :param n:
        :return:
        """
        def dfs(path, cur_left, cur_right, left_left, left_right):
            if left_left == 0 and left_right == 0:
                ans.append(path)
                return
            if cur_left > cur_right:
                dfs(path + ')', cur_left, cur_right + 1, left_left, left_right - 1)
            if left_left > 0:
                dfs(path + '(', cur_left + 1, cur_right, left_left - 1, left_right)

        ans = []
        path = '('
        dfs(path, 1, 0, n - 1, n)
        return ans


s = Solution()
print(s.generateParenthesis(2))
