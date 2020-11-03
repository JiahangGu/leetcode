#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/26 10:09
# @Author:JiahangGu

chn_num = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
chn_unit_section = ["", "万", "亿", "万亿"]
chn_unit = ["", "十", "百", "千"]


def arabic2chn(num):
    if num == 0:
        return "零"
    unit_pos = 0
    need_zero = False
    ans = []
    while num > 0:
        section = num % 10000
        if need_zero:
            ans.insert(0, chn_num[0])
        section_nums = []
        # 转换小节并在后续加上对应节权位
        section2chn(section, section_nums)
        section_nums.append(chn_unit_section[unit_pos] if section != 0 else chn_unit_section[0])
        ans.insert(0, "".join(section_nums))
        # 用于后续判断是否需要补0，条件是小节内的数字小于1000
        need_zero = 0 < section < 1000
        num //= 10000
        unit_pos += 1
    return "".join(ans)


def section2chn(section, section_nums):
    unit_pos = 0
    # 用于标记个位数开始的连续零不需要处理
    zero = True
    while section > 0:
        v = section % 10
        if v:
            # 标记小节前面如果出现0需要补零
            zero = False
            chn_num_char = chn_num[v] + chn_unit[unit_pos]
            section_nums.insert(0, chn_num_char)
        else:
            # 只有后面有数字且当前为0才会补零
            if not zero:
                zero = True
                section_nums.insert(0, chn_num[0])
        unit_pos += 1
        section //= 10


print(arabic2chn(2000100190))
