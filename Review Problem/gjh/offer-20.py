#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/2 17:01
# @Author:JiahangGu


class Solution:
    def isNumber(self, s: str) -> bool:
        """
        判断是否数值的关键是满足以下条件
        1.+-必须出现在第一位或e的后一位
        2.如果出现小数点，之前不能有小数点和E出现
        3.如果出现E，之前不能有E出现或没有数字出现
        4.如果出现非法字符，直接返回
        5.最终数字必须要出现
        可以设定flag表示小数点、E以及数字是否出现
        :param s:
        :return:
        """
        s = s.strip()
        dot_flag, e_flag, num_flag = False, False, False
        for i in range(len(s)):
            if s[i] == '-' or s[i] == '+':
                if not (i == 0 or s[i-1] == 'E' or s[i-1] == 'e'):
                    return False
            elif s[i] == '.':
                if dot_flag or e_flag:
                    return False
                dot_flag = True
            elif s[i] == 'E' or s[i] == 'e':
                if not num_flag or e_flag:
                    return False
                e_flag = True
                num_flag = False
            elif '0' <= s[i] <= '9':
                num_flag = True
            else:
                return False
        if not num_flag:
            return False
        return True


s = Solution()
print(s.isNumber("46.e3"))
