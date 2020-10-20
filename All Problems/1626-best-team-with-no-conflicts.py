#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/19 14:42
# @Author:JiahangGu
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        首先注意到矛盾的定义是age[i]>age[j]且score[i]<score[j]。考虑到可以在有序序列上
        通过递增关系直接确定升降序，所以可以选择对ages或scores排序，在遍历时可以得到一个有序的
        序列，此时只需要判断另一维度是否满足要求。
        假设对age排序，则得到age升序结果且要在age相同时scores升序。这样保证在对下一位判断是否矛盾时，
        只需要检验score是否符合要求。
        然后设dp[i]表示以i结尾的球队所能得到的最大分数，假设j遍历[0:i]，如果j和i不矛盾，则更新
        dp[i] = max(dp[i], dp[j] + scores[i])，表示在j的球队上加上i。
        最终结果是max(dp)
        :param scores:
        :param ages:
        :return:
        """
        def cmp(a, b):
            if a[1] == b[1]:
                if a[0] < b[0]:
                    return -1
                else:
                    return 1
            elif a[1] < b[1]:
                return -1
            else:
                return 1

        from functools import cmp_to_key
        l = []
        for i in range(len(scores)):
            l.append([scores[i], ages[i]])
        l.sort(key=cmp_to_key(cmp))
        ans = 0
        dp = [0] * len(scores)
        for i in range(len(l)):
            dp[i] = l[i][0]
            for j in range(i):
                if l[j][0] <= l[i][0] or l[j][1] == l[i][1]:
                    dp[i] = max(dp[i], dp[j] + l[i][0])
            ans = max(ans, dp[i])
        return ans
