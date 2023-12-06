import re
import polars as pl
from functools import reduce


with open("input.txt") as f:
    lines = f.readlines()

time = [x for x in re.findall(r'\d+', lines[0])]
distance = [x for x in re.findall(r'\d+', lines[1])]

time = [int(reduce(lambda x, y: x + y, time))]
distance = [int(reduce(lambda x, y: x + y, distance))]

nr_ways_to_win = []

for game in range(len(time)):
    speed = pl.Series(list(range(time[game]+1)))
    time_left = pl.Series(list(range(time[game], -1, -1)))
    nr_ways_to_win.append(sum(speed * time_left > distance[game]))

print(reduce(lambda x, y: x * y, nr_ways_to_win))
