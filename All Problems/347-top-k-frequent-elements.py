#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/7 10:44
# @Author:JiahangGu
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        首先统计数字的出现频数，然后对频数排序得到前k个。由于要求时间复杂度优于O(nlgn)，快排、归并等排序算法不能使用。
        可以使用的排序算法有如下几种（可以参考Sort/模板整理.doc)
        1.堆排序：构造一个k个元素的最小堆，堆的调整复杂度为O(lgk)，总复杂度为O(nlgk)
        2.计数排序：需要得到整个频数的范围，这里不确定是多大，但复杂度为O(n+k)
        3.二叉搜索树：构造一个含有k个节点的二叉搜索树，使用类似于堆排序的操作
        :param nums:
        :param k:
        :return:
        """
        # def min_heapify(nums, start, end):
        #     father = start
        #     son = 2 * start + 1
        #     while son <= end:
        #         if son + 1 <= end and nums[son][1] > nums[son+1][1]:
        #             son += 1
        #         if nums[father][1] > nums[son][1]:
        #             nums[son], nums[father] = nums[father], nums[son]
        #         father = son
        #         son = 2 * father + 1
        #
        # max_value, min_value = max(nums), min(nums)
        # freq = [0] * (max_value - min_value + 1)
        # for num in nums:
        #     freq[num-min_value] += 1
        # cnt = 0
        # index = 0
        # min_heap = []
        # while cnt < k:
        #     if freq[index]:
        #         min_heap.append((index+min_value, freq[index]))
        #         cnt += 1
        #     index += 1
        # for i in range((k-1)//2, -1, -1):
        #     min_heapify(min_heap, i, k-1)
        # for i in range(index, len(freq)):
        #     if freq[i] and freq[i] > min_heap[0][1]:
        #         min_heap[0] = (i+min_value, freq[i])
        #         min_heapify(min_heap, 0, k-1)
        # ans = []
        # for index, freq in min_heap:
        #     ans.append(index)
        # return ans
        """
        可以使用优先队列实现同样效果。
        此外还可以利用快排中分区的思想，求出分区之后的index，如果index<k则表示k在右边，继续分区，如果index>k则k在左边，
        对左边继续分区，直到k=index，此时数组的前k位则是满足要求的答案，注意这里是对频数降序排序。
        """
        # def partition(nums, l, r):
        #     pivot = nums[l]
        #     while l < r:
        #         while l < r and nums[r][1] < pivot[1]:
        #             r -= 1
        #         if l < r:
        #             nums[l] = nums[r]
        #         while l < r and nums[l][1] >= pivot[1]:
        #             l += 1
        #         if l < r:
        #             nums[r] = nums[l]
        #     nums[l] = pivot
        #     return l
        #
        # max_value, min_value = max(nums), min(nums)
        # freq = [0] * (max_value - min_value + 1)
        # for num in nums:
        #     freq[num-min_value] += 1
        # sorted_nums = []
        # for i in range(len(freq)):
        #     if freq[i]:
        #         sorted_nums.append((i+min_value, freq[i]))
        # l = 0
        # r = len(sorted_nums) - 1
        # idx = partition(sorted_nums, l, r)
        # while l < r:
        #     if idx < k:
        #         l = idx + 1
        #     elif idx > k:
        #         r = idx - 1
        #     else:
        #         break
        #     if l < r:
        #         idx = partition(sorted_nums, l, r)
        # ans = [sorted_nums[i][0] for i in range(k)]
        # return ans
        """
        也可以使用计数排序
        """
        import math
        max_value, min_value = max(nums), min(nums)
        freq = [0] * (max_value - min_value + 1)
        for num in nums:
            freq[num - min_value] += 1
        sorted_nums = []
        for i in range(len(freq)):
            if freq[i]:
                sorted_nums.append((i + min_value, freq[i]))
        max_digits = math.ceil(math.log(max(freq), 10))
        bucket = [[] for _ in range(10)]
        for i in range(max_digits):
            for item in sorted_nums:
                idx = item[1] % (10 ** (i+1)) // (10 ** i)
                bucket[idx].append(item)
            sorted_nums.clear()
            for j in range(9, -1, -1):
                sorted_nums.extend(bucket[j])
            bucket = [[] for _ in range(10)]
        return [sorted_nums[i][0] for i in range(k)]


s = Solution()
nums = [5,1,-1,-8,-7,8,-5,0,1,10,8,0,-4,3,-1,-1,4,-5,4,-3,0,2,2,2,4,-2,-4,8,-7,-7,2,-8,0,-8,10,8,-8,-2,-9,4,-7,6,6,-1,4,2,8,-3,5,-9,-3,6,-8,-5,5,10,2,-5,-1,-5,1,-3,7,0,8,-2,-3,-1,-5,4,7,-9,0,2,10,4,4,-4,-1,-1,6,-8,-9,-1,9,-9,3,5,1,6,-1,-2,4,2,4,-6,4,4,5,-5]
k = 7
print(s.topKFrequent(nums, k))
