class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ''' 这个方法在有负数的情况下就错了，比如[-1,0] -1，因为要用到比-1大的数
        left = 0
        right = len(numbers) - 1
        while left < right:
            mid = left + (right-left+1)//2
            if numbers[mid] > target:
                right = mid - 1
            else:
                left = mid
        flag = left #小于等于target的最大值坐标

        left = 0
        right = flag
        ans = []
        while left < right:
            if numbers[left] + numbers[right] > target:
                right = right - 1
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            else:
                ans.append(left+1)
                ans.append(right+1)
                return ans
        '''

        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right = right - 1
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            else:
                return [left+1,right+1]
