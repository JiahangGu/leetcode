#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/27 14:07
# @Author:JiahangGu
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        滑动窗口解法。记录一个区间，这个区间是不存在重复字符的。如果新访问的字符在区间已经出现，则根据此前记录的
        字符位置，更新当前最大解，并更新窗口区间。
        注意滑动窗口在需要更新之前，最大解应更新为当前窗口大小。此外，还需要判断最右边界的字符是出现在整个字符串中
        还是出现在当前窗口中，如果不在窗口中那么直接加入到窗口即可
        :param s:
        :return:
        """
        if not s:
            return 0
        pos = dict()
        l, r = 0, 0
        pos[s[0]] = 0
        ans = 1
        while r < len(s) - 1:
            r += 1
            if r == len(s) - 1:
                if s[r] not in pos or pos[s[r]] < l:
                    ans = max(ans, r - l + 1)
                else:
                    ans = max(ans, r - l)
                break
            if s[r] not in pos or pos[s[r]] < l:
                pos[s[r]] = r
            else:
                ans = max(ans, r - l)
                l = pos[s[r]] + 1
                pos[s[r]] = r
        return ans


s = Solution()
print(s.lengthOfLongestSubstring("aabaab!bb"))
