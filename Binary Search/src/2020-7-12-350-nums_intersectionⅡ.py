from typing import List
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        找两个数组的交集，元素出现次数与在数组中一致，使用计数的方法，对较短数组每个元素出现次数计数，然后在较长数组中寻找是否有已计数的元素，若有则加入答案，并把元素的计数次数减1
        :param nums1:
        :param nums2:
        :return:
        '''
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        c = collections.Counter()
        for num in nums1:
            c[num] += 1

        ans = []
        for num in nums2:
            if c[num] > 0:
                ans.append(num)
                c[num] -= 1
        return ans

    def sort_intersect(self,nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        进阶：给定数组有序，则用两个指针从数组第一个元素开始遍历，逐个比较，若相等则加入答案，如不相等则把较小的元素的指针加1
        '''
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        i, j = 0, 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans



s = Solution()
ans = s.sort_intersect([1,2],[1,1])
print(ans)
