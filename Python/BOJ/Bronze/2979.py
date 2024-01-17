a, b, c = map(int, input().split())
car = []
ans = 0
for i in range(3):
    car.append(list((map(int, input().strip().split()))))

car.sort()
first = car[0][0]
car2 = sorted(car, key = lambda x: x[1])
last = car2[2][1]

for i in range(first+1, last+1):
    cnt = 0
    if car[0][0] < i and car[0][1] >= i:
        cnt += 1
    if car[1][0] < i and car[1][1] >= i:
        cnt += 1
    if car[2][0] < i and car[2][1] >= i:
        cnt += 1
    if cnt == 1:
        ans += a
    elif cnt == 2:
        ans += b * 2
    elif cnt == 3:
        ans += c * 3

print(ans)