T = int(input())
R,S = input().split()
R = int(R)
P = ""
while T != 0:
    for j in range(len(S)):
        P = P + (S[j] * R)
    print(P)
    T-=1
    if T == 0:
        break
    R,S = input().split()
    R = int(R)
    P = ""