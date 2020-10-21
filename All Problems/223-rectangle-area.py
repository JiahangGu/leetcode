#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/20 22:09
# @Author:JiahangGu
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        """
        比较两个矩形的左下角和右上角坐标关系，分情况讨论不同情况下的重叠面积
        :param A:
        :param B:
        :param C:
        :param D:
        :param E:
        :param F:
        :param G:
        :param H:
        :return:
        """
        ans = 0
        if E <= A and F <= B:
            if G <= A or H <= B:
                ans = 0
            elif G >= C and H >= D:
                ans = (C - A) * (D - B)
            elif G <= C and H >= D:
                ans = (G - A) * (D - B)
            elif G >= C and H <= D:
                ans = (C - A) * (H - B)
            elif G <= C and H <= D:
                ans = (G - A) * (H - B)
        elif E >= A and F <= B:
            if H <= B or C <= E:
                ans = 0
            elif G >= C and H >= D:
                ans = (C - E) * (D - B)
            elif G <= C and H >= D:
                ans = (G - E) * (D - B)
            elif G >= C and H <= D:
                ans = (C - E) * (H - B)
            elif G <= C and H <= D:
                ans = (G - E) * (H - B)
        elif E <= A and F >= B:
            if G <= A or D <= F:
                ans = 0
            elif G >= C and H >= D:
                ans = (C - A) * (D - F)
            elif G <= C and H >= D:
                ans = (G - A) * (D - F)
            elif G >= C and H <= D:
                ans = (C - A) * (H - F)
            elif G <= C and H <= D:
                ans = (G - A) * (H - F)
        elif E >= A and F >= B:
            if C <= E or D <= F:
                ans = 0
            elif G >= C and H >= D:
                ans = (C - E) * (D - F)
            elif G <= C and H >= D:
                ans = (G - E) * (D - F)
            elif G >= C and H <= D:
                ans = (C - E) * (H - F)
            elif G <= C and H <= D:
                ans = (G - E) * (H - F)
        return (C - A) * (D - B) + (G - E) * (H - F) - ans


s = Solution()
print(s.computeArea(1282,-1386,1290,-1380,1284,-1384,1296,-1375))
