#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/27 17:45
# @Author:JiahangGu
class Solution:
    def intToRoman(self, num: int) -> str:
        """
        也是考察模拟的做法，首先对数字各位数进行切分，除了4， 40， 400， 9， 90， 900之外剩余的数字只需要
        构建对应的字符串即可。这些特殊字符同理，只是字符位置不同。
        不涉及算法，不再实现
        :param num:
        :return:
        """