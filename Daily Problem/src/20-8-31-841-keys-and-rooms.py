#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/2 21:46
# @Author:JiahangGu
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        DFS。从0号房间开始，拿房间的每一把钥匙直到无法进入房间回溯。并使用标记数组标明每个房间是否
        可以进入，在结束时若每个都可以进入则返回True。注意这里的标记数组是用于最后计算结果，而不是
        访问过就不再进入，如[[1,2],[],[]]的情况，需要从0号进入两次，所以需要在用完一把钥匙后从列
        表中删除，房间没有钥匙作为递归结束条件。
        :param rooms:
        :return:
        """
        # def dfs(cur_room):
        #     room_visit_flag[cur_room] = True
        #     if not rooms[cur_room]:
        #         return
        #     while rooms[cur_room]:
        #         next_room = rooms[cur_room].pop(0)
        #         dfs(next_room)
        #
        # room_visit_flag = [False] * len(rooms)
        # dfs(0)
        # for flag in room_visit_flag:
        #     if not flag:
        #         return False
        # return True
        """
        此外还可以使用BFS的方法进行搜索，相比于DFS的做法来说，BFS每次直接取出该房间的所有钥匙，存入栈中，再进入
        栈中有钥匙的房间进行循环，这样就不用担心一个房间有多个钥匙重复进入多次的情况。注意这里标记的时候，在拿到
        钥匙后就标记为True表示该房间可以到达，不然会出现此前的多个房间含有进入同一房间的钥匙，但由于该房间还未进
        入，会重复记录钥匙，虽然不会对结果有影响，但是增加了时间花销。
        """
        stack = [0]
        room_visit_flag = [False] * len(rooms)
        room_visit_flag[0] = True
        while stack:
            cur_key = stack.pop(0)
            for key in rooms[cur_key]:
                if not room_visit_flag[key]:
                    room_visit_flag[key] = True
                    stack.append(key)
        for flag in room_visit_flag:
            if not flag:
                return False
        return True


s = Solution()
print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
