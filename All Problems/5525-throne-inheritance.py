#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/27 13:12
# @Author:JiahangGu
from typing import List


class ThroneInheritance:

    def __init__(self, kingName: str):
        from collections import defaultdict
        self.order = defaultdict(list)
        self.order[kingName] = []
        self.king = kingName
        self.death_flag = defaultdict(bool)

    def birth(self, parentName: str, childName: str) -> None:
        self.order[parentName].append(childName)

    def death(self, name: str) -> None:
        self.death_flag[name] = True

    def getInheritanceOrder(self) -> List[str]:
        ans = []

        def dfs(root):
            if not self.death_flag[root]:
                ans.append(root)
            for child in self.order[root]:
                dfs(child)

        dfs(self.king)
        return ans

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
