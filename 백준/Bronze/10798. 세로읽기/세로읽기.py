strAll = []
cnt = 0
for i in range(5):
    strAll.append(list(input()))
while cnt <= 15:
    for j in strAll:
        if len(j) > cnt:
            print(j[cnt],end="")
    cnt+=1