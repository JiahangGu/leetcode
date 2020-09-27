#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/4 15:49
# @Author:JiahangGu


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        分别记录连续出现的0和1的个数，符合要求的子串的数量为二者的最小值，然后在下一次记录时，如果1结尾则置0个数为0，
        0结尾则置1个数为0.
        :param s:
        :return:
        """
        # num0 = 0
        # num1 = 0
        # ans = 0
        # for i in range(len(s)-1):
        #     if s[i] == '0':
        #         num0 += 1
        #     elif s[i] == '1':
        #         num1 += 1
        #     if s[i] != s[i+1]:
        #         if s[i] == '0':
        #             ans += min(num0, num1)
        #             num1 = 0
        #         elif s[i] == '1':
        #             ans += min(num0, num1)
        #             num0 = 0
        # if s[-1] == '0':
        #     num0 += 1
        # else:
        #     num1 += 1
        # ans += min(num0, num1)
        # return ans
        """
        看官方题解发现，不需要在意当前字符是0还是1，只要判断连续出现的值即可，那么可以省去判断是0和1的语句，在常数项
        方面是一个优化。
        """
        last = 0
        ans = 0
        s_ptr = 0
        while s_ptr < len(s):
            count = 0
            char = s[s_ptr]
            while s_ptr < len(s) and s[s_ptr] == char:
                count += 1
                s_ptr += 1
            ans += min(count, last)
            last = count
        return ans


s = Solution()
print(s.countBinarySubstrings("00110011"))
