import polars as pl

with open("input.txt") as f:
    lines = f.readlines()


winners = []
numbers = []

for card in lines:

    winners.append(card.rstrip().split("|")[0].split(" "))
    numbers.append(card.rstrip().split("|")[1].split(" "))

win = []

for card in winners:
    win.append([x for x in card if x.isdigit()])

num = []

for card in numbers:
    num.append([x for x in card if x.isdigit()])

matches = []

for i in range(len(win)):
    matches.append(len(set(win[i]) & set(num[i])))

matches = pl.Series(matches)

print( pl.Series([1 * 2 ** (i-1) for i in matches if i > 0]).sum() )