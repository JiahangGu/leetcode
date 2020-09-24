#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/24 21:35
# @Author:JiahangGu
class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        首先根据/对路径进行切分，判断//之间的是什么，如果是文件名，放入栈中，如果是.跳过，如果是..弹出栈。
        并且要删除连续的/。
        :param path:
        :return:
        """
        stack = []
        idx = 0
        while idx < len(path):
            while idx < len(path) and path[idx] == '/':
                idx += 1
            tmp = ''
            while idx < len(path) and path[idx] != '/':
                tmp += path[idx]
                idx += 1
            if tmp == '..':
                if stack:
                    stack.pop()
            elif tmp == '.' or tmp == '':
                continue
            else:
                stack.append(tmp)
        ans = ""
        for file in stack:
            ans = ans + '/' + file
        return ans if ans != '' else '/'


s = Solution()
path = "/a//b////c/d//././/.."
print(s.simplifyPath(path))
