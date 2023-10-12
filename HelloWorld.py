# from cs50 import get_float, get_int, get_string

print("hello, world again")
# answer = get_string("What's your name : ")  # not by default
answer = input("What's your name : ")
print(f"hello, {answer}")

counter = 0
counter += 1  # counter++ and counter-- does not exist
x = 0
y = 2
if x < y:  # no paranthesis () needed, but can do if needed
    print("x is less")
elif y > x:
    print("y is less")
else:
    print("both are same")

# while True:  # False
#     print("Something")

i = 0
while i < 3:
    print("while something")
    i += 1

for j in [0, 1, 2]:
    print("for j something")


n = 10
for k in range(n):  # 0 to n-1
    print("for k something")

for l in range(5, n):  # 5 to n-1
    print("for l something")

# data types : bool, float, int, str (no longer integer overflow), floating point error still possible

# range, list, tuple(x,y), dict("a":1) , set

# to run : python3 hello.py

# to run c : clang -o hello hello.c -lcs50
# ./hello

# c : source code -> compiler
# py : source code -> interpreter (can be a little slower this way, as it is in a diff language than what computer understand)
