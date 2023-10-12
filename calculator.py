from cs50 import get_int
# import cs50
# x = get_int("x : ")
# y = get_int("y : ")
# print(x+y)

a = input("a : ")
b = input("b : ")
# print(a+b)  # returns string joining ab
try:
    print(int(a)+int(b))  # fails if a non-numeric value provided
# except:
except ValueError:
    print("non numeric values")
    exit()

z = int(a)/int(b)
# z = int(a)//int(b) like in c
print(z)
print(f"{z:.50f}")
