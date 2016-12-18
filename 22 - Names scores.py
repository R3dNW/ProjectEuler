import utilities

with open("p022_names.txt", "r") as f:
    names = f.read().split(",")

names_alpha_value = {}

for i in range(0, len(names)):
    names[i] = names[i].strip("\",./'\n").lower()

    alpha_value = 0

    for char in names[i]:
        alpha_value += utilities.alphabet.index(char) + 1

    names_alpha_value[names[i]] = alpha_value

names_score = {}

names = sorted(names)

for i in range(0, len(names)):
    names_score[names[i]] = names_alpha_value[names[i]] * (i+1)

print(names_score)

print(sum(names_score.values()))
