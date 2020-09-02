#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/28 17:39
# @Author:JiahangGu

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        统计对应移动的次数，相等即可回来
        :param moves:
        :return:
        """
        move_num = dict()
        for c in moves:
            move_num[c] = move_num.get(c, 0) + 1
        if move_num.get("U", 0) == move_num.get("D", 0) and move_num.get("R", 0) == move_num.get("L", 0):
            return True
        return False


s = Solution()
print(s.judgeCircle("UD"))
