#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/20 15:19
# @Author:JiahangGu
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
        首先可以使用暴力解法，对于每个元素查询前面的k个元素是否差值小于t的数字。时间复杂度为O(nmin(n,k))。
        但是会超时，因为每一个元素查询前k个是重复的，可以通过记录此前的k个元素的大小关系使每次查询为lgk的复杂度。
        例如使用AVL树，插入和删除元素都是O(lgk)，查询时查找是否存在小于abs(nums[i]-t)的元素时间复杂度也是O(lgk)，
        但AVL树还不会，暂时搁置。

        此外还有桶排序的做法。既然要求k范围内存在小于等于t的数字，可以以t+1为桶大小，划分为若干个桶，将nums[i]取索引放入
        对应桶中，在滑动时，如果对应索引桶中有元素，或者相邻桶中存在满足条件的元素，则返回True。否则继续滑动，并将左侧窗口元素
        弹出。放入右侧元素。
        需要注意，由于可能存在负数元素，所以应该以最小值作为桶的起点。
        :param nums:
        :param k:
        :param t:
        :return:
        """
        def get_id(num, x, minmum):
            return int((num - minmum) / x)

        if k <= 0:
            return False
        from collections import defaultdict
        buckets = defaultdict(list)
        start = 0
        minmum = min(nums)
        for i in range(len(nums)):
            idx = get_id(nums[i], t + 1, minmum)
            if len(buckets[idx]) > 0:
                return True
            if len(buckets[idx + 1]) and abs(buckets[idx + 1][0] - nums[i]) <= t:
                return True
            if idx != 0 and len(buckets[idx - 1]) and abs(buckets[idx - 1][0] - nums[i]) <= t:
                return True
            if i - start >= k:
                start_idx = get_id(nums[start], t + 1, minmum)
                buckets[start_idx].pop()
                start += 1
            buckets[idx].append(nums[i])
        return False


s = Solution()
nums = [2147483647,-1,2147483647]
k = 1
t = 2147483647
print(s.containsNearbyAlmostDuplicate(nums, k, t))
