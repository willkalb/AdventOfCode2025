import Helper
DAY = "6"

lines = [ [ s for s in l.split(" ") if len(s) > 0 ] for l in Helper.get_input_lines(DAY) ]

total_sum = 0
for c in range(0, len(lines[0])):
    total_sum += eval(lines[len(lines) - 1][c].join([ lines[r][c] for r in range(0, len(lines)) if lines[r][c].isdigit() ]))

print(f"\tPart 1: {total_sum}")

lines = [ " " + s for s in Helper.get_input_lines_preserve_space(DAY) ]

total_sum = 0
nums = []
for c in range(len(lines[0]) - 1, -1, -1):
    curr_num = "".join([ lines[r][c] for r in range(0, len(lines)) if lines[r][c].isdigit() ])

    if len(curr_num) > 0:
        nums.append(curr_num)
        continue

    total_sum += eval(lines[len(lines) - 1][c + 1].join(nums))
    nums = []

print(f"\tPart 2: {total_sum}")
