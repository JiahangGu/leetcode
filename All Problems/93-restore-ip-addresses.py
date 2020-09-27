#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/4 15:49
# @Author:JiahangGu
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        回溯算法，从起始点开始，判断s[0],s[01],s[012]是否可以构成一个ip地址的整数，如果可以则当前
        整数个数+1，并递归进入后续剩余字符串。
        递归结束条件：k>4并且剩余字符串为空，如果k==4但字符串不空则不成立剪枝，如果字符串为空但k<4则不成立
        剪枝
        :param s:
        :return:
        """
        def back_track(string, k, path):
            if not string and k == 4:
                ans.append(".".join(path))
                return
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


s = Solution()
print(s.restoreIpAddresses("101023"))
