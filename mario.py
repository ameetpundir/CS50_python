def main():
    height = get_height()
    for i in range(height):
        # print("#")
        print("?", end="")  # named argument : end
    print()
    # can also be dones as below
    print("#" * height)
    print()


def get_height():
    while True:
        try:
            n = int(input("What should be the height : "))
            if (n > 0):
                break
        except ValueError:
            print("Invalid Input")

    return n


main()
