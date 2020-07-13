#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/13 9:30
# @Author:JiahangGu
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        '''
        归并排序统计逆序对的解法，两个分别有序的数组，AB，从后向前遍历，如果A的数字大，则
        B中小于该数字的个数为B剩余的元素个数，A指针前移，否则B指针前移。
        需要注意的是，需要申请一个临时变量数组，来保留排序后的结果，并在统计完成
        后更新对应索引的原数组。理由是将数组拆分成两部分归并排序，递归进入到最小
        数组时停止，可以保证在统计时，左右两侧数组已经有序，并且不改变数字的前后
        位置关系，不会对解产生影响。
        最终完成计算后原数组应该为有序状态。
        在上述解法的基础上，新增了一个难点是数字位置是在排序过程中发生变化的，所以需要记录
        一个索引数组来保存排序后的索引。此外，还需要一个数组来记录最终的结果，更新方式依赖
        于对应数字的索引。
        :param nums:
        :return:
        '''
        n = len(nums)
        idx = [i for i in range(n)]
        ans = [0] * n
        tmp_idx = [None] * n
        temp = [None] * n

        def merge(left, right):
            if left >= right:
                return
            mid = (left + right) // 2
            merge(left, mid)
            merge(mid+1, right)
            l, r, merge_idx = mid, right, right
            while l >= left and r >= mid + 1:
                if nums[r] >= nums[l]:
                    temp[merge_idx] = nums[r]
                    tmp_idx[merge_idx] = idx[r]
                    r -= 1
                else:
                    ans[idx[l]] += (r - mid)
                    temp[merge_idx] = nums[l]
                    tmp_idx[merge_idx] = idx[l]
                    l -= 1
                merge_idx -= 1
            while l >= left:
                temp[merge_idx] = nums[l]
                tmp_idx[merge_idx] = idx[l]
                l -= 1
                merge_idx -= 1
            while r >= mid + 1:
                temp[merge_idx] = nums[r]
                tmp_idx[merge_idx] = idx[r]
                r -= 1
                merge_idx -= 1
            nums[left:right+1] = temp[left:right+1]
            idx[left:right+1] = tmp_idx[left:right+1]
            return

        merge(0, n-1)
        return ans


s = Solution()
x = [5, 2, 6, 1]
print(s.countSmaller(x))
