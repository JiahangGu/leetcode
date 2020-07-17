class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        判断一个正整数是否为完全平方数，与69题类似，使用二分寻找它的完全平方根，若找到则返回TRUE，若循环结束还没找到则返回False
        注意num为1的时候没有进入循环，但它是完全平方数，所以单独考虑
        :param num:
        :return:
        '''
        if num == 1:
            return True
        left = 1
        right = num // 2
        while left < right:
            mid = left + (right - left + 1) // 2
            sqrt = mid * mid

            if sqrt > num:
                right = mid - 1
            elif sqrt == num:
                return True
            else:
                left = mid
        return False


