#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/27 13:13
# @Author:JiahangGu
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = []
        for path in logs:
            if path == '../':
                if s:
                    s.pop()
            elif path == './':
                continue
            else:
                s.append(path)
        return len(s)
