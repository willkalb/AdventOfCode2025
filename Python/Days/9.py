import Helper

DAY = "9"


coords = [ (tuple(map(int, l.split(",")))[:2]) for l in Helper.get_input_lines(DAY) ]

max_area = 0
for i in range(0, len(coords)):
    c = coords[i]
    for ii in range(i + 1, len(coords)):
        cc = coords[ii]
        l_max = abs(c[0] - cc[0] + 1) * abs(c[1] - cc[1] + 1)
        if max_area > l_max:
            continue

        max_area = l_max

print(f"\tPart 1: {max_area}")

max_area = 0
for i in range(0, len(coords)):
    pass

print(f"\tPart 2: {max_area}")
