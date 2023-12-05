import polars as pl
import re

df = pl.scan_csv(
    "input.txt",
    has_header=False,
    separator="\t",
    new_columns=["input"],
    dtypes=[pl.Utf8],
).collect()

new = []


for codeword in df["input"]:

    code_list = []

    for combo in (
        ("1", "one"),
        ("2", "two"),
        ("3", "three"),
        ("4", "four"),
        ("5", "five"),
        ("6", "six"),
        ("7", "seven"),
        ("8", "eight"),
        ("9", "nine"),
    ):
        number_pos = [m.start() for m in re.finditer(combo[0], codeword)]
        word_pos = [m.start() for m in re.finditer(combo[1], codeword)]

        if number_pos:
            for position in number_pos:
                code_list.append((combo[0], position))
        if word_pos:
            for position in word_pos:
                code_list.append((combo[0], position))

    new.append(code_list)


for item in new:
    item.sort(key=lambda a: a[1])

first = pl.Series([i[0][0] for i in new])
last = pl.Series([i[-1][0] for i in new])


result = first + last
print(result.cast(pl.Int64).sum())
