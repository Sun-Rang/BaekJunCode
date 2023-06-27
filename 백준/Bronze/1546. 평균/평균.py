num = int(input())
sejun = list(map(int,input().split()))
A = []
sejun_max = max(sejun)
for score in sejun:
    A.append(score/sejun_max*100)
print(sum(A) / num)