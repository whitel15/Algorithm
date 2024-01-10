import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
stack = []

for i in range(n):
    cmd = input().strip()
    if cmd[1] == "u":
        num = list(cmd.split())
        stack.append(num[1])
    elif cmd == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            num = stack.pop()
            print(num)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])