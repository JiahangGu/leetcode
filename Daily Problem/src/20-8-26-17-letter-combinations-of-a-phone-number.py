#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/28 16:21
# @Author:JiahangGu
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        回溯算法。每次遍历当前数字对应的字符集合进入下一层递归，直到递归结束记录当前字符串为解，回溯。
        :param digits:
        :return:
        """
        def back_tracking(left_digits, path):
            if not left_digits:
                ans.append("".join(path))
                return
            for char in chars[left_digits[0]]:
                path.append(char)
                back_tracking(left_digits[1:], path)
                path.pop()

        if not digits:
            return []
        ans = []
        chars = dict()
        chars["2"] = ["a", "b", "c"]
        chars["3"] = ["d", "e", "f"]
        chars["4"] = ["g", "h", "i"]
        chars["5"] = ["j", "k", "l"]
        chars["6"] = ["m", "n", "o"]
        chars["7"] = ["p", "q", "r", "s"]
        chars["8"] = ["t", "u", "v"]
        chars["9"] = ["w", "x", "y", "z"]
        back_tracking(digits, [])
        return ans


s = Solution()
print(s.letterCombinations(""))
