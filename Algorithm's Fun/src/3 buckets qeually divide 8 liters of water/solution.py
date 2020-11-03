#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/26 11:38
# @Author:JiahangGu

from copy import deepcopy

class Action:
    def __init__(self, f, t, water):
        self.f = f
        self.t = t
        self.water = water


class State:
    def __init__(self, buckets, action):
        self.buckets = buckets
        self.action = action


class Solution:
    def __init__(self):
        self.full_buckets = [8, 5, 3]
        self.bucket_num = 3
        self.ans = []
        self.flag = [[[False for _ in range(4)] for _ in range(6)] for _ in range(9)]

    def equally_divide(self):
        def is_end(cur_state):
            return cur_state.buckets[0] == 4 and cur_state.buckets[1] == 4 and cur_state.buckets[2] == 0

        def print_ans(states):
            print("Answer {}:".format(len(self.ans) + 1))
            for state in states:
                if state.action:
                    print("Dump " + str(state.action.water) + " liters of water from " + str(state.action.f) +
                          " to " + str(state.action.t))

        def visited(state):
            return self.flag[state.buckets[0]][state.buckets[1]][state.buckets[2]]

        def can_dump_water(state, f, t):
            if state.buckets[f] > 0 and state.buckets[t] < self.full_buckets[t]:
                return True
            return False

        def dump_water(state, f, t):
            new_state = deepcopy(state)
            to_be_dump = self.full_buckets[t] - state.buckets[t]
            if state.buckets[f] >= to_be_dump:
                new_state.buckets[f] -= to_be_dump
                new_state.buckets[t] += to_be_dump
            else:
                new_state.buckets[t] += state.buckets[f]
                to_be_dump = state.buckets[f]
                new_state.buckets[f] = 0
            if to_be_dump > 0:
                new_action = Action(f, t, to_be_dump)
                new_state.action = new_action
                return new_state
            return None

        def search_action(states, state, f, t):
            if can_dump_water(state, f, t):
                next_state = dump_water(state, f, t)
                if next_state and not visited(next_state):
                    self.flag[state.buckets[0]][state.buckets[1]][state.buckets[2]] = True
                    states.append(next_state)
                    search_state(states)
                    states.pop()
                    self.flag[state.buckets[0]][state.buckets[1]][state.buckets[2]] = False

        def search_state(states):
            cur_state = states[-1]
            if is_end(cur_state):
                print_ans(states)
                self.ans.append(states[:])
                return
            for i in range(self.bucket_num):
                for j in range(self.bucket_num):
                    if i != j:
                        search_action(states, cur_state, i, j)

        init_state = State([8, 0, 0], None)
        self.flag[8][0][0] = True
        search_state([init_state])


s = Solution()
s.equally_divide()
print(len(s.ans))
