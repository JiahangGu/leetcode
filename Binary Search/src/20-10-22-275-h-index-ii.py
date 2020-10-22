#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/22 23:28
# @Author:JiahangGu
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        如果是降序排列，则只要找到最左边满足i >= nums[i]的i即可，但给定是升序排列，需要找到不满足
        n-i-1 >= nums[i]且最靠左的i，这样h指数的结果为：1.如果l满足h指数定义则返回n-l；否则返回最小的值，因为
        上述不满足说明所有数值都相同。
        :param citations:
        :return:
        """
        # n = len(citations)
        # if n == 0:
        #     return 0
        # l, r = 0, n - 1
        # while l < r:
        #     mid = l + (r - l) // 2
        #     if n - mid - 1 >= citations[mid]:
        #         l = mid + 1
        #     else:
        #         r = mid
        # if n - l <= citations[l]:
        #     return n - l
        # else:
        #     return citations[0]
        """
        给定一个大小为 n 的升序的引用次数列表，要求找到满足 citations[i] >= n - i 的第一个 citations[i]
        首先，我们先获取列表的中间元素，即 citations[pivot]，它将原始列表分成了两个子列表：citations[0 : pivot - 1] 和 citations[pivot + 1 : n]。
        然后比较 n - pivot 和 citations[pivot] 的值，二分搜索算法分为以下 3 种情况：
        若 citations[pivot] == n - pivot：则我们找到了想要的元素。
        若 citations[pivot] < n - pivot：由于我们想要的元素应该大于或等于 n - pivot，所以我们应该进一步搜索右边的子列表，即 citations[pivot + 1 : n]。
        若 citations[pivot] > n - pivot：我们应该进一步搜索左边的子列表，即 citations[0 : pivot-1]
        """
        n = len(citations)
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if n - mid == citations[mid]:
                return n - mid
            elif n - mid < citations[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return n - l


s = Solution()
print(s.hIndex([11]))
