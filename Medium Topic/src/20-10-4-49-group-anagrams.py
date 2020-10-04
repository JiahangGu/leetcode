#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 15:29
# @Author:JiahangGu
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        对每个字符串排序，相同的放一起即可。
        或者记录字符串中各字符的出现频率，相同的放一起。
        :param strs:
        :return:
        """