# words = dict()  # hash table

words = set()


def check(word):
    if word.lower() in words:
        return True
    else:
        return False


def load(dic):  # dic is a string which takes the path of the files
    # inbuilt py function which opens a file in read mode
    file = open(dic, "r")
    for line in file:
        word = line.rstrip()
        words.add(word)
    file.close()
    return True


def size():
    return len(words)


def unload():
    return True  # nothing to do, no freeing needed
