S = input().upper()
A = set(S)
C = []
max = 0
cnt = 0
for i in A:
    if S.count(i) > max:
        max = S.count(i)
for j in A:
    if S.count(j) == max:
        cnt+=1
        C.append(j)
if cnt > 1:
    print("?")
else:
    print(C[0])