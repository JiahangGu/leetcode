#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/15 9:30
# @Author:JiahangGu
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        使用长除法求解这个问题，长除法就是在不够除的时候在后面补0，即列竖式的解法。
        求循环部分的做法需要注意到既然除数是固定的，那么期间出现过的商如果已经出现过，剩余的部分
        一定是循环的，证明是一个无限循环小数。而当余数为0时则是有限小数。
        难度不高，但是需要考虑很多种情况。例如除数或被除数为0，结果是负数，从商的某一个位置开始循环而不是一开始，
        :param numerator:
        :param denominator:
        :return:
        """
        if denominator == 0 or numerator == 0:
            return "0"
        flag = False
        if (denominator < 0 and numerator > 0) or (denominator > 0 and numerator < 0):
            flag = True
        numerator = abs(numerator)
        denominator = abs(denominator)
        ans = []
        num1 = numerator // denominator
        ans.append(str(num1))
        reminder = numerator % denominator
        if reminder == 0:
            if flag:
                return "-" + ans[0]
            else:
                return ans[0]
        ans.append(".")
        pos = dict()
        idx = 2
        while reminder:
            if reminder in pos:
                ans.insert(pos[reminder], "(")
                ans.append(")")
                break
            pos[reminder] = idx
            idx += 1
            reminder *= 10
            num1 = reminder // denominator
            ans.append(str(num1))
            reminder %= denominator
        if flag:
            ans.insert(0, "-")
        return "".join(ans)


s = Solution()
numerator = 1
denominator = 6
print(s.fractionToDecimal(numerator, denominator))
