#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/28 22:37
# @Author:JiahangGu
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        从初始点开始，找到所有初始像素的连通图，将连通图中的点替换为新的像素值
        :param image:
        :param sr:
        :param sc:
        :param newColor:
        :return:
        """
        def fillColor(x, y, row, col, oldColor, newColor):
            if 0 <= x < row and 0 <= y < col and image[x][y] == oldColor and image[x][y] != newColor:
                image[x][y] = newColor
                fillColor(x-1, y, row, col, oldColor, newColor)
                fillColor(x+1, y, row, col, oldColor, newColor)
                fillColor(x, y-1, row, col, oldColor, newColor)
                fillColor(x, y+1, row, col, oldColor, newColor)
        row = len(image)
        if row == 0:
            return image
        col = len(image[0])
        fillColor(sr, sc, row, col, image[sr][sc], newColor)
        return image
