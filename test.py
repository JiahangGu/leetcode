#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/29 10:03
# @Author:JiahangGu
from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        degree = [0] * n
        for i in range()


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()


s = Solution()
n = 3
requests = [[1,2],[0,0],[0,2],[0,1],[0,0],[0,2],[1,0],[0,1],[2,0]]
print(s.maximumRequests(n, requests))
