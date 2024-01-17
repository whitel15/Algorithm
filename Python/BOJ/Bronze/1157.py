word = input().strip()
count = [0] * 26
cnt = 0
idx = 0

for i in word:
    if i >= "a" and i <= "z":
        count[ord(i)-97] += 1
    else:
        count[ord(i)-65] += 1

for i in range(len(count)):
    if count[i] == max(count):
        cnt += 1
        idx = i

if cnt > 1:
    print("?")
else:
    print(chr(65+idx))