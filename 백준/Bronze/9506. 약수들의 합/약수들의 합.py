n = int(input())
while n != -1:
    b = []
    for i in range(1,n+1):
        if n % i == 0:
            b.append(i)
    if sum(b[:-1]) == n:
        print(f"{n} = {b[0]}",end="")
        for j in range(1,len(b)-1):
            print(f" + {b[j]}",end="")
        print()
    else:
        print(f"{n} is NOT perfect.")
    n = int(input())