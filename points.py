from cs50 import get_int

points = get_int("ur points : ")

if points < 2:
    print("Less than me")
elif points > 2:
    print("More than me")
else:
    print("Same as me")
