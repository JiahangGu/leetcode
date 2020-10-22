#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/22 20:41
# @Author:JiahangGu
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        H指数指至少h个大于等于h的数，并且其余数字不大于h。首先对数组降序排序，则对于当前数字nums[i]，至少有
        i个数字大于等于nums[i]，如果出现i >= nums[i]的情况则是满足条件的h指数，且是最大的。
        :param citations:
        :return:
        """
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if i >= citations[i]:
                return i
        return len(citations)
