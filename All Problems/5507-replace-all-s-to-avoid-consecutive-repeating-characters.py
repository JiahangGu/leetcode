#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/6 10:31
# @Author:JiahangGu


class Solution:
    def modifyString(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            if s[i] == '?':
                tmp = set()
                if i != 0:
                    tmp.add(s[i-1])
                    tmp.add(ans[i-1])
                if i != len(s) - 1:
                    tmp.add(s[i+1])
                for j in range(ord('a'), ord('z')+1):
                    if chr(j) not in tmp:
                        ans += chr(j)
                        break
            else:
                ans += s[i]
        return ans


s = Solution()
print(s.modifyString("??yw?ipkj?"))
