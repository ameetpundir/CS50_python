# s = input("Do you agree : ")
s = input("Do you agree : ").lower()
# if s.lower in ["y", "yes"]:  # and so on, same for no
if s in ["y", "yes"]:  # and so on, same for no

    # if s in ["y", "Y", "yes", "Yes"]:  # and so on, same for no
    # if s == "Y" or s == "y":
    print("Agree")

if s == "N" or s == "n":
    print("Do Not Agree")
