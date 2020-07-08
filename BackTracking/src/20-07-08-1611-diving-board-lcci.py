#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/8 9:51
# @Author:JiahangGu
from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        '''
        需要注意的点是
        1.k==0时没有解
        2.shorter==longer时只有一种解
        3.要求是从小到大排序，所以应该从全部都是shorter的开始，每次去掉一根shorter加上longer，
        可以保证递增序并且没有重复解
        :param shorter:
        :param longer:
        :param k:
        :return:
        '''
        if k == 0:
            return []
        ans = []
        if shorter == longer:
            return [k * shorter]
        for i in range(k + 1):
            ans.append(i * longer + (k - i) * shorter)
        return ans


def test():
    s = Solution()
    ans = s.divingBoard(1,2,3)
    print(ans)
