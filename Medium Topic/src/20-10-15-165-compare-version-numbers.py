#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/15 9:09
# @Author:JiahangGu
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        按照.划分为数字序列后，首先去除前导0，然后比较两个数字的大小。
        需要注意的是版本号是递增数字，而不是比较字符串，例如1.10大于1.2.因为10>2.
        :param version1:
        :param version2:
        :return:
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        while v1 or v2:
            if v1:
                s1 = int(v1.pop(0))
            else:
                s1 = 0
            if v2:
                s2 = int(v2.pop(0))
            else:
                s2 = 0
            if s1 > s2:
                return 1
            elif s1 < s2:
                return -1
        return 0


s = Solution()
version1 = "1.2"
version2 = "1.10"
print(s.compareVersion(version1, version2))
