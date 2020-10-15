#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/15 9:41
# @Author:JiahangGu
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        题目要求是找到在字符串中出现次数大于一次的序列，例如一个[i:j]序列在[pos+i:pos+j]也出现，则是出现多次
        可以使用滑动窗口维护一个size为10的窗，并对窗口内的字符串用哈希存储，如果出现过则是重复序列。
        :param s:
        :return:
        """
        start = 0
        size = 10
        ans = set()
        hash_table = set()
        while start + size <= len(s):
            tmp = s[start:start+size]
            if tmp in hash_table:
                ans.add(tmp)
            else:
                hash_table.add(tmp)
            start += 1
        return list(ans)


s = Solution()
print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))
