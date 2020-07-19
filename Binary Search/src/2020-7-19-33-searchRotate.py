from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        找出目标数在经过旋转后的有序数组中的位置，重点在于对判断条件的修改来决定舍弃右区间还是左区间
        通过一些输出样例，总结出需要判断以下三个数的大小关系：nums[left],nums[mid],target
        针对舍弃右区间的情况：
        当nums[left]<=target<=nums[mid]时，如[4,5,6,7,0,1,2],5
        当target<=nums[mid]<nums[left]时，如[6,7,0,1,2,4,5],0
        当nums[mid]<nums[left]<=target时，如[5,6,7,0,1,2,4],7
        则舍弃右区间，right=mid-1
        其余情况下均舍弃左区间，left=mid+1

        题解中给出了一个极其简单的判别式：异或，对三个不等式，若两个为真则整体为假，若一个为真则整体为真，不会存在三个都为真或都为假的情况
        :param nums:
        :param target:
        :return:
        '''
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left+1)//2
            if nums[mid] == target:
                return mid
            if (nums[left]<=target) ^ (target<=nums[mid]) ^ (nums[mid]<nums[left]):\
                left = mid + 1
            else:
                right = mid - 1
        return -1

s = Solution()
ans = s.search([4,5,6,7,0,1,2],5)
print(ans)