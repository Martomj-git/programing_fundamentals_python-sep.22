num1 = int(input())
for i in range(num1):
    num2 = int(input())
    if num2 % 2 != 0:
        print(f'{num2} is odd!')
        break
else:
    print("All numbers are even.")
