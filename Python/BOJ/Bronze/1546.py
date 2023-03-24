num = int(input())
A = list()
A = input().split()
sum = 0
max = 0

for i in range(num):
    if int(A[i])>max :
        max = int(A[i])
    sum = sum + int(A[i])

print(sum/max*100/num)