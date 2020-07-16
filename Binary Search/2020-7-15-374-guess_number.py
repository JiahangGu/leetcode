# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        '''
        猜数字的大小，给出的guess接口是你在猜数字的时候用到的，最后需要返回猜对的数字，guess返回1表示你猜的数字大了，返回-1表示你猜的数字笑了，返回0表示猜到的数字正确
        :param n:
        :return:
        '''
        left = 1
        right = n
        while left < right:
            mid = left + (right-left+1)//2
            if guess(mid) == -1:
                right = mid - 1
            else:
                left = mid
        return left