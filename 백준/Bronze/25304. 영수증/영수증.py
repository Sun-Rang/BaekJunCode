X = int(input())
N = int(input())
price = 0
for i in range(N):
    item_price, buy = map(int,input().split())
    price = price + (item_price * buy)
if X == price:
    print("Yes")
else:
    print("No")