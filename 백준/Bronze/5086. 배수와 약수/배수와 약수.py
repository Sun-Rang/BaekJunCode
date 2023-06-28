num1,num2 = map(int,(input().split()))

while num1 != 0 and num2 != 0:
    list = []
    if num1 < num2:
        for i in range(1,num2):
            if num2 % i == 0:
                list.append(i)
        if num1 in list:
            print("factor")
        else:
            print("neither")
    elif num1 > num2:
        if num1 % num2 == 0:
            print("multiple")
        else:
            print("neither")
    num1,num2 = map(int,(input().split()))