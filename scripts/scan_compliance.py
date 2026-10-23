#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合规扫描：政治敏感、色情、暴恐/违法教程、仇恨歧视、真实个人信息。
用法：python3 scan_compliance.py chapters/ch177.md [...]
输出最后一行 命中=N
"""
import re
import sys

RULES = [
    ('政治', [
        '国家主席', '总书记', '中央政治局', '人民代表大会', '国务院', '政协',
        '总统', '首相', '总理', '执政党', '在野党', '大选', '公投', '领土争议',
    ]),
    ('色情', [
        '性交', '做爱', '裸体', '乳房', '下体', '阴茎', '阴道', '情色', '淫',
    ]),
    ('暴恐违法', [
        '制作炸弹', '炸药配方', '土制炸弹', '制毒', '冰毒配方', '枪支改装',
        '洗钱流程', '伪造证件教程', '入侵教程',
    ]),
    ('仇恨歧视', [
        '劣等民族', '种族清洗', '灭绝人种', '支那', '黑鬼',
    ]),
    ('真实个人信息', [
        '身份证号', '银行卡号', '手机号码', '家庭住址',
    ]),
]


def scan(path):
    hits = []
    with open(path, encoding='utf-8') as f:
        lines = f.read().split('\n')
    for i, line in enumerate(lines, 1):
        for cat, words in RULES:
            for w in words:
                if w in line:
                    hits.append((i, cat, w, line.strip()))
    return hits


def main():
    total = 0
    for path in sys.argv[1:]:
        hits = scan(path)
        total += len(hits)
        print('== %s : 命中=%d' % (path, len(hits)))
        for ln, cat, w, ctx in hits:
            print('  L%-4d [%s] %s | %s' % (ln, cat, w, ctx[:60]))
    print('命中=%d' % total)


if __name__ == '__main__':
    main()
