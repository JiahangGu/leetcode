#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/11/3 19:58
# @Author:JiahangGu
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        """
        首先需要注意的是累加数至少包含3个数，每个数字的位数不确定，所以可以明确是一个回溯算法，主要是对第一和第二个数
        进行回溯，第一个数和第二个数的长度均应该小于第三个数的长度。一旦确定第一二个数字之后剩余的序列是可以确定的。
        此外，可能是大数相加，所以不能使用普通的数字，而是使用大数加法。
        解法可以轻易想出来，但存在很多细节问题需要处理。
        1.序列中的数不会以0开头，所以以0开头且长度大于1的数字被认为是非法的，例如"02"
        2.遍历的情况的划分，由于是枚举第一个和第二个数字的对应位置，已知第一个数字长度为i的情况下，
        第二个数字的长度应为[1,(n-i)//2]，闭区间
        3.所有长度小于等于2的输入均为False，得不到3个数字。
        :param num:
        :return:
        """
        def big_add(s1, s2):
            if len(s1) < len(s2):
                s1, s2 = s2, s1
            ans = ""
            c = 0
            i = len(s2) - 1
            j = len(s1) - 1
            while i >= 0:
                tmp = int(s2[i]) + int(s1[j]) + c
                c = tmp // 10
                ans += str(tmp % 10)
                i -= 1
                j -= 1
            while c or j >= 0:
                if j == -1:
                    ans += str(c)
                    break
                tmp = int(s1[j]) + c
                c = tmp // 10
                ans += str(tmp % 10)
                j -= 1
            return ans[::-1]

        def dfs(pos, pos1, pos2):
            if pos2 >= n - 1:
                return True
            num1, num2 = num[pos:pos1 + 1], num[pos1 + 1:pos2 + 1]
            if num1[0] == '0' or num2[0] == '0':
                return False
            num3 = big_add(num1, num2)
            pos3 = pos2 + len(num3)
            x = num[pos2 + 1:pos3 + 1]
            if num3 == x:
                return dfs(pos1+1, pos2, pos3)
            else:
                return False

        n = len(num)
        for i in range(n // 2):
            for j in range(1, (n - i + 1) // 2):
                if dfs(0, i, i + j):
                    return True
        return False


s = Solution()
print(s.isAdditiveNumber("199001200"))
