import re

with open("input.txt") as f:
    lines = f.readlines()

possible_games = []

for index, line in enumerate(lines, 1):
    
    red = max([int(x.replace(' red', '')) for x in re.findall('\d{1,2} (?:red?)', line)])
    green = max([int(x.replace(' green', '')) for x in re.findall('\d{1,2} (?:green?)', line)])
    blue = max([int(x.replace(' blue', '')) for x in re.findall('\d{1,2} (?:blue?)', line)])

    possible_games.append(red * green * blue)

print(possible_games)
print(sum(possible_games))