#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/6 9:30
# @Author:JiahangGu
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        暴力法，逐个拼接字符串然后判断是否回文，判断回文可以根据从两边向中间收缩。
        :param words:
        :return:
        """
        # def is_palindrome(s):
        #     if len(s) <= 1:
        #         return True
        #     left, right = 0, len(s)-1
        #     while left < right:
        #         if s[left] != s[right]:
        #             return False
        #         left += 1
        #         right -= 1
        #     return True
        # ans = []
        # for i in range(len(words)):
        #     for j in range(i+1, len(words)):
        #         if is_palindrome(words[i] + words[j]):
        #             ans.append([i, j])
        #         if is_palindrome(words[j] + words[i]):
        #             ans.append([j, i])
        # return ans
        """
        意料中的超时，探索一下优化的方向。考虑到这里要判断的是两个字符串的拼接，可以在拼接之前对字符串进行
        一些处理
        假设两个字串a, b，拼接时分为如下情况：
        1.a.length==b.length，这样如果要拼接起来是回文串则ab互为逆序
        2.a.length<>b.length，假设a比b长，则a应该分为a1, a2两部分，且a1为回文串，且a2与b互为逆序，这里
        还要考虑到换位置拼接的情况
        如果遍历所有字符串组合，时间复杂度O(N^2)，再按照如上逻辑判断，最坏情况下（字符串长度差极端）复杂度
        依然是O(N^2*M)，只是M由平均长度变为了差的平均值。
        可以考虑用长度来遍历，如果长度为j的部分是回文串，那么剩余部分的逆序存在则拼接起来可以构成回文串。
        注意空字符串对结果产生的影响，首先字符串数组里可能存在空串，不能直接去掉，且要保证空串也要遍历一次，
        所以遍历的长度范围为[0, len(s)+1），如果为空也能遍历一次。
        然后以bat，tab为例，bat从空开始查找发现tab存在，存入结果[1,0]，如果遍历到tab，则第二部分为空，也是
        回文串，但是这个串的结果依然为[1,0]，即leftId=0，所以存在重复，解决办法就是在第二个空的时候不遍历，
        即增加判断条件，如果是遍历到第二个部分为空，由于已经查找过第一部分为空的情况，所以跳过。
        """
        def is_palindrome(s):
            if len(s) <= 1:
                return True
            left, right = 0, len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        ans = []
        pos = {words[i][::-1]: i for i in range(len(words))}
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m+1):
                if is_palindrome(word[:j]):
                    rightId = pos.get(word[j:], -1)
                    if rightId != -1 and rightId != i:
                        ans.append([rightId, i])
                if j != m and is_palindrome(word[j:]):
                    leftId = pos.get(word[:j], -1)
                    if leftId != -1 and leftId != i:
                        ans.append([i, leftId])
        return ans


s = Solution()
x = ["bat","tab","cat"]
print(s.palindromePairs(x))
