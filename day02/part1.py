import re

with open("input.txt") as f:
    lines = f.readlines()

possible_games = []

for index, line in enumerate(lines, 1):
    if (
        (max([int(x.replace(' red', '')) for x in re.findall('\d{1,2} (?:red?)', line)]) <= 12) &
        (max([int(x.replace(' green', '')) for x in re.findall('\d{1,2} (?:green?)', line)]) <= 13) &
        (max([int(x.replace(' blue', '')) for x in re.findall('\d{1,2} (?:blue?)', line)]) <= 14)
    ):
        possible_games.append(index)

print(possible_games)
print(sum(possible_games))