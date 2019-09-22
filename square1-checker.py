#!/usr/bin/env python
# coding: utf-8

""" square-1の上下面どちらかの側面が、簡単な操作で揃えられるかを確認するためのプログラム """

import argparse
import copy
from collections import deque

N = 8

def swap(s, pos):
    # 隣り合う二個のペア同士を入れ替える操作
    ret = copy.deepcopy(s)
    ret[pos], ret[(pos+2)%N] = ret[(pos+2)%N], ret[pos]
    ret[(pos+1)%N], ret[(pos+3)%N] = ret[(pos+3)%N], ret[(pos+1)%N]
    return ret

def shift(s, n):
    # n*90度回転 (swapの繰り返しでshiftもできるので必要なかった)
    return s[n*2:] + s[:n*2]


def get_next_states(s):
    # ある側面の状態からswapもしくはshiftで遷移できる全ての状態を返す
    ret = []
    for i in range(N):
        ret.append(swap(s, i))
    for i in range(N//2):
        if i == 0:
            continue
        ret.append(shift(s, i))
    return ret

def main():
    # 側面が揃った状態を初期状態とする
    start = ["r", "rb", "b", "bo", "o", "oy", "y", "yr"]

    # 側面が揃った状態からたどり着ける状態を列挙する
    hash_table = set()
    hash_table.add("".join(start))
    queue = deque([])
    queue.append(start)
    while len(queue) > 0:
        s = queue.popleft()
        states = get_next_states(s)
        for ns in states:
            ns_hash = "".join(ns)
            if ns_hash in hash_table:
                continue
            queue.append(ns)
            hash_table.add(ns_hash)

    # ある側面が、簡単な操作の繰り返しで側面を揃った状態にできるかの確認
    print("rboboyyyrorb" in hash_table)
    print("brbryrooyybo" in hash_table)

if __name__ == '__main__':
    main()

