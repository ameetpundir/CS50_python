from cs50 import get_int
# scores = [72, 73, 33]
scores = []

for i in range(3):
    score = get_int("Scores : ")
    # scores.append(score)
    scores = scores + [score]
    # scores += [score]

average = sum(scores) / len(scores)

print(average)
