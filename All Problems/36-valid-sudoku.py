#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/29 10:35
# @Author:JiahangGu
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        使用三个字典记录每行、每列以及每个3*3宫格内出现的数字，对于每个遍历到的新数字，判断是否出现即可。
        :param board:
        :return:
        """