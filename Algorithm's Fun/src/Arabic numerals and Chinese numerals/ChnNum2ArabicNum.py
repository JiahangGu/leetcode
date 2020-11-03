#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/26 10:09
# @Author:JiahangGu


chn_value_pair = {"十": (10, False), "百": (100, False), "千": (1000, False),
                  "万": (10000, True), "亿": (100000000, True)}
arabic_num = {"零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八":8, "九": 9}


def chn2arabic(chn_string):
    ans = 0
    section = 0
    number = 0
    pos = 0
    while pos < len(chn_string):
        # 数字返回对应数，单位返回-1
        num = arabic_num[chn_string[pos]] if chn_string[pos] in arabic_num else -1
        if num >= 0:
            number = num
            pos += 1
            if pos == len(chn_string):
                section += number
                ans += section
                break
        else:
            unit, sec_unit = chn_value_pair[chn_string[pos]]
            if sec_unit:
                section = (section + number) * unit
                ans += section
                section = 0
            else:
                section += number * unit
            pos += 1
            number = 0
            if pos == len(chn_string):
                ans += section
                break
    return ans


print(chn2arabic("二十亿零一十万零一百九十"))