#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/5 9:28
# @Author:JiahangGu
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        回溯算法，当前数字范围是有效的话就作为一个候选，剩余字符串进入深层递归。
        :param s:
        :return:
        """
        def back_track(string, k, path):
            if not string and k == 4:
                ans.append(".".join(path))
            if k == 4 or not string:
                return
            if string and '0' <= string[0] <= '9':
                path.append(string[0])
                back_track(string[1:], k+1, path)
                path.pop()
            if len(string) >= 2 and '10' <= string[:2] <= '99':
                path.append(string[:2])
                back_track(string[2:], k+1, path)
                path.pop()
            if len(string) >= 3 and '100' <= string[:3] <= '255':
                path.append(string[:3])
                back_track(string[3:], k+1, path)
                path.pop()

        if len(s) > 12:
            return []
        ans = []
        back_track(s, 0, [])
        return ans
