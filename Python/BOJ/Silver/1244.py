import sys
input = sys.stdin.readline

Sn = int(input())
switch = list(map(int, input().split()))
Cn = int(input())
Student = []

for i in range(Cn):
    a, b = map(int, input().split())
    Student.append((a, b))


def Mswitch(x):
    if switch[x] == 0:
        switch[x] = 1
    else:
        switch[x] = 0


for i in range(Cn):
    sex = Student[i][0]
    num = Student[i][1]

    if sex == 1:
        for j in range(Sn):
            if (j + 1) % num == 0:
                Mswitch(j)

    else:
        idx = num - 1
        Mswitch(idx)
        left = idx - 1
        right = idx + 1
        while 1:
            if 0 <= left and right < Sn and switch[left] == switch[right]:
                Mswitch(left)
                Mswitch(right)
                left -= 1
                right += 1
            else:
                break

for i in range(Sn):
    if i in (20, 40, 60, 80):
        print(" ")
    print(switch[i], end=" ")
