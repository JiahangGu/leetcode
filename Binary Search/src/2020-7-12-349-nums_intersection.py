from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        找两个数组的交集，不重复，先用set去重，再从长度短的数组开始遍历元素，判断每一个元素是否在另一个数组中，如果是则返回
        :param nums1:
        :param nums2:
        :return:
        '''
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1)<len(set2):
            return [x for x in set1 if x in set2]
        else:
            return [x for x in set2 if x in set1]

s = Solution()
ans = s.intersection([1,2,2,1],[2,2])
print(ans)