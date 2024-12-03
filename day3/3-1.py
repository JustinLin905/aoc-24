import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "3.txt")

res = 0
do = True

with open(file_path, "r") as f:
    raw_text = f.read().strip()
    p = re.compile(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)")
    commands = p.findall(raw_text)
    print(commands)

    for c in commands:
        if c.startswith("mul") and do:
            comma_index = c.index(",")
            close_bracket_index = c.index(")")
            x = int(c[4:comma_index])
            y = int(c[comma_index + 1 : close_bracket_index])

            res += x * y
        else:
            do = True if c == "do()" else False

print(res)
