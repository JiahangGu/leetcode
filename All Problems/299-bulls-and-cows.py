#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/11/3 16:09
# @Author:JiahangGu
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        哈希做法，统计数字出现频率，如果位置相同则单独记录，剩下的数字统计一共有多少位置错误的。
        :param secret:
        :param guess:
        :return:
        """
        from collections import defaultdict
        ans1, ans2 = 0, 0
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                ans1 += 1
            else:
                hash1[secret[i]] += 1
                hash2[guess[i]] += 1
        for i in range(10):
            ans2 += min(hash1[str(i)], hash2[str(i)])
        return str(ans1) + "A" + str(ans2) + "B"


s = Solution()
secret = "1123"
guess = "4111"
print(s.getHint(secret, guess))
