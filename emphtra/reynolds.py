'''
计算雷诺数
此处只是列出了最简单的计算公式，后续再进一步细化
单独建立该文件主要是考虑到使用的比较多
'''


def reynolds_number(p, miu, D, n):
    return p * miu * D / n
