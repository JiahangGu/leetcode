#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/26 20:16
# @Author:JiahangGu

from copy import deepcopy


class Action:
    def __init__(self, boat_to, monster, monk):
        self.boat_to = boat_to
        self.monster = monster
        self.monk = monk


class State:
    def __init__(self, local_monster=0, local_monk=0, remote_monster=0, remote_monk=0, boat_pos=0, action=None):
        self.local_monster = local_monster
        self.local_monk = local_monk
        self.remote_monster = remote_monster
        self.remote_monk = remote_monk
        # 0表示在本侧河岸，1表示在对岸
        self.boat_pos = boat_pos
        self.action = action


class Solution:
    def __init__(self):
        # 去河对岸标记为0，回来为1
        self.actions = [Action(0, -1, 0), Action(0, -2, 0), Action(0, 0, -1), Action(0, 0, -2), Action(0, -1, -1),
                        Action(1, 1, 0), Action(1, 2, 0), Action(1, 0, 1), Action(1, 0, 2), Action(1, 1, 1)]
        self.ans = []
        self.flag = [[[[[False for _ in range(2)] for _ in range(4)] for _ in range(4)] for _ in range(4)] for \
                     _ in range(4)]
        self.monster_cnt = 3
        self.monk_cnt = 3

    def cross_river(self):
        def is_end(state):
            return state.local_monster == 0 and state.local_monk == 0 and state.remote_monster == 3 and \
                   state.remote_monk == 3 and state.boat_pos == 1

        def print_ans(states):
            print("Answer {}:".format(len(self.ans) + 1))
            for state in states:
                if state.action:
                    if state.action.boat_to == 0:
                        print("{} monsters, {} monks cross river".format(abs(state.action.monster),
                                                                         abs(state.action.monk)))
                    else:
                        print("{} monsters, {} monks get back".format(abs(state.action.monster),
                                                                      abs(state.action.monk)))

        def is_valid(state):
            return (state.local_monster <= state.local_monk or state.local_monk == 0) and (
                    state.remote_monster <= state.remote_monk or state.remote_monk == 0)

        def visited(state):
            return self.flag[state.local_monster][state.local_monk][state.remote_monster][state.remote_monk][state.boat_pos]

        def can_take_action(state, action):
            if state.boat_pos != action.boat_to:
                return False
            if state.local_monster + action.monster < 0 or state.local_monster + action.monster > self.monster_cnt:
                return False
            if state.local_monk + action.monk < 0 or state.local_monk + action.monk > self.monk_cnt:
                return False
            return True

        def get_next_state(state, action):
            if can_take_action(state, action):
                new_state = State()
                new_state.action = action
                new_state.local_monster = state.local_monster + action.monster
                new_state.local_monk = state.local_monk + action.monk
                new_state.remote_monster = state.remote_monster - action.monster
                new_state.remote_monk = state.remote_monk - action.monk
                new_state.boat_pos = 1 - action.boat_to
                return new_state
            return None

        def search_action(states, state, action):
            next_state = get_next_state(state, action)
            if next_state and is_valid(next_state) and not visited(next_state):
                self.flag[state.local_monster][state.local_monk][state.remote_monster][state.remote_monk][
                    state.boat_pos] = True
                states.append(next_state)
                search_state(states)
                states.pop()
                self.flag[state.local_monster][state.local_monk][state.remote_monster][state.remote_monk][
                    state.boat_pos] = False

        def search_state(states):
            cur_state = states[-1]
            if is_end(cur_state):
                print_ans(states)
                self.ans.append(states[:])
                return
            for i in range(len(self.actions)):
                search_action(states, cur_state, self.actions[i])

        init_state = State(3, 3, 0, 0, 0)
        self.flag[3][3][0][0][0] = True
        search_state([init_state])


s = Solution()
s.cross_river()
print(len(s.ans))