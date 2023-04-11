from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())


def is_prime(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True


def subin(num):
    if is_prime(num):
        if len(str(num)) == n:
            print(num)
        else:
            for i in range(1, 10, 2):
                subin(num * 10 + i)


subin(2)
subin(3)
subin(5)
subin(7)
