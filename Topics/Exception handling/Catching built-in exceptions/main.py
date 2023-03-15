a = int(input())
b = int(input())
try:
    result = float(a // b)
except ZeroDivisionError:
    print("The Error!")
else:
    print(result)