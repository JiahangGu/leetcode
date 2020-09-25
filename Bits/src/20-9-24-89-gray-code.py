#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/24 21:54
# @Author:JiahangGu
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        先尝试暴力解法，设置flag，标记各编码是否出现，还需要求编码数字用作结果记录
        :param n:
        :return:
        """
        # def get_num(code):
        #     ans = 0
        #     for i in range(len(code)):
        #         if code[i] == '1':
        #             ans += int(pow(2, i))
        #     return ans
        #
        # def dfs(path, s):
        #     if len(path) == target:
        #         return True
        #     for i in range(len(s)):
        #         x = s[i]
        #         s[i] = str(1-int(x))
        #         tmp = "".join(s)
        #         if not flag[tmp]:
        #             path.append(get_num(tmp))
        #             flag[tmp] = True
        #             if dfs(path, s):
        #                 return True
        #             flag[tmp] = False
        #         s[i] = x
        #     return False
        #
        # target = pow(2, n)
        # from collections import defaultdict
        # flag = defaultdict(bool)
        # ans = [0]
        # s = ['0'] * n
        # flag["".join(s)] = True
        # dfs(ans, s)
        # return ans
        """
        可以通过，但耗时很久，仅击败7.86.考虑一下优化的方向。
        首先是不需要对编码每次都求一次对应数值，因为只修改一位，判断01加减该数字2的幂次即可。
        时间快了4ms，此外没有明显地改进点。
        """
        # def dfs(path, s):
        #     if len(path) == target:
        #         return True
        #     for i in range(len(s)):
        #         x = s[i]
        #         s[i] = str(1-int(x))
        #         tmp = "".join(s)
        #         if not flag[tmp]:
        #             last = path[-1]
        #             if s[i] == '0':
        #                 last -= pow(2, i)
        #             else:
        #                 last += pow(2, i)
        #             path.append(last)
        #             flag[tmp] = True
        #             if dfs(path, s):
        #                 return True
        #             path.pop()
        #             flag[tmp] = False
        #         s[i] = x
        #     return False
        #
        # target = pow(2, n)
        # from collections import defaultdict
        # flag = defaultdict(bool)
        # ans = [0]
        # s = ['0'] * n
        # flag["".join(s)] = True
        # dfs(ans, s)
        # return ans
        """
        找规律法。格雷码特点是相邻码只有一个二进制位不同，则假设g(n)为n阶格雷码集合，若要拓展到n+1阶，只需
        在g(n)前加0，并且将g(n)倒序前加1，将二者拼接。拼接处只有第一位不同，而两个子集则同样满足相邻位只有一个
        二进制位不同。起始为g(0)=[0]
        """
        ans = [0]
        bit = 1
        for i in range(1, n+1):
            for j in range(len(ans) - 1, -1, -1):
                ans.append(bit + ans[j])
            bit <<= 1
        return ans


s = Solution()
print(s.grayCode(2))
