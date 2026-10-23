#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""硬指标扫描：破折号、禁用字、裸对白提示、不是X是Y、章末钩子。
用法：python3 scan_hard_indicators.py chapters/ch177.md [...]
输出最后一行 block=N
"""
import re
import sys

BAN_CHARS = {'很': '禁用字', '被': '禁用字', '发': '禁用字'}

# 破折号（含全角长横、em dash、en dash）
DASH = re.compile(r'——|—|–')

# 引号前裸「某某说」：可选标点 + 1-3 个汉字 + 说/道/问/答 + 可选冒号 + 引号
BARE_TAG = re.compile(r'[，。！？：]?[\u4e00-\u9fa5]{1,3}(?:说|道|问|答|喊|叫)[：:]?\s*[“"]')

# 不是 X 是 Y
NOT_X_BUT_Y = re.compile(r'不是[^。！？\n“”]{0,15}[，、]?[而]?是')

# 章末禁升华：结尾句里出现这些抽象词
LIFT = ['命运', '宿命', '意义', '救赎', '灵魂', '永恒', '一切', '从此', '终于明白', '他懂了']


def scan(path):
    blocks = []
    with open(path, encoding='utf-8') as f:
        lines = f.read().split('\n')

    for i, line in enumerate(lines, 1):
        if i == 1 and line.startswith('# '):
            continue
        for ch, kind in BAN_CHARS.items():
            for m in re.finditer(ch, line):
                blocks.append((i, kind, '禁用字「%s」' % ch, line.strip()))
        for m in DASH.finditer(line):
            blocks.append((i, '破折号', '破折号', line.strip()))
        for m in BARE_TAG.finditer(line):
            blocks.append((i, '裸对白', '引号前裸提示语：%s' % m.group(0), line.strip()))
        for m in NOT_X_BUT_Y.finditer(line):
            blocks.append((i, '句式', '不是X是Y：%s' % m.group(0), line.strip()))

    # 章末钩子：最后 3 个非空行
    tail = [l for l in lines if l.strip()][-3:]
    for l in tail:
        for w in LIFT:
            if w in l:
                blocks.append((len(lines), '升华', '章末抽象词「%s」' % w, l.strip()))

    return blocks


def main():
    total = 0
    for path in sys.argv[1:]:
        blocks = scan(path)
        total += len(blocks)
        print('== %s : block=%d' % (path, len(blocks)))
        for ln, kind, msg, ctx in blocks:
            print('  L%-4d [%s] %s | %s' % (ln, kind, msg, ctx[:60]))
    print('block=%d' % total)


if __name__ == '__main__':
    main()
