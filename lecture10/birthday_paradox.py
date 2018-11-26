#!usr/bin/python3
# Birthday paradox

import random

def has_dup(A):
    N = len(A)
    for i in range(N):
        for j  in range(1 + i, N):
            if A[i] == A[j]:
                return True
    return False


def birthdays(student_count):
    a = []
    for i in range(student_count):
        a.append(random.randint(1, 365))
    return a

def paradox_check(try_num, student_count):
    n = 0
    for i in range(try_num):
        if has_dup(birthdays(student_count)):
            n += 1
    print(f"students: {student_count}, tries: {try_num}, tries succeded: {n}")

paradox_check(1000, 23)
