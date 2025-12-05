import Helper
DAY = "5"

lines = Helper.get_input_lines(DAY)

fresh_ranges = []
ids = []

for line in lines:
    if len(line) == 0:
        continue
    
    if "-" in line:
        fresh_ranges.append(tuple([ int(l) for l in line.split("-") ]))
        continue
    
    ids.append(int(line))

fresh_ids = []
for id in ids:
    for low, high in fresh_ranges:
        if id >= low and id <= high:
            fresh_ids.append(id)
            break

print(f"\tPart 1: {len(fresh_ids)}")


for r in range(0, len(fresh_ranges) - 1):
    for rr in range(r + 1, len(fresh_ranges)):
        if fresh_ranges[r] == None or fresh_ranges[rr] == None:
            continue
        
        r_low, r_high = fresh_ranges[r]
        rr_low, rr_high = fresh_ranges[rr]

        # r     |----
        # rr    |----
        if r_low == rr_low:
            # r     ----|
            # rr    ----|
            if r_high == rr_high:
                fresh_ranges[rr] = None
                continue

            # r     --|
            # rr    ----|
            if r_high < rr_high:
                fresh_ranges[r] = None
                break

            # r     ----|
            # rr    --|
            if r_high > rr_high:
                fresh_ranges[rr] = None
                continue

        # r     ----|
        # rr    ----|
        if r_high == rr_high:
            # r       |--
            # rr    |----
            if r_low > rr_low:
                fresh_ranges[r] = None
                break

            # r     |----
            # rr      |--
            if r_low < rr_low:
                fresh_ranges[rr] = None
                continue

        # r     |----
        # rr      |--
        if r_low < rr_low and rr_low < r_high:
            # r     --|
            # rr    ----|
            if r_high < rr_high:
                fresh_ranges[rr] = (r_high + 1, rr_high)
                continue

            # r     ----|
            # rr    --|
            if r_high > rr_high:
                fresh_ranges[rr] = None
                continue

        # r       |--
        # rr    |----
        if rr_low < r_low and r_low < rr_high:
            # r     --|
            # rr    ----|
            if r_high < rr_high:
                fresh_ranges[r] = None
                break

            # r     ----|
            # rr    --|
            if r_high > rr_high:
                fresh_ranges[rr] = (rr_low, r_low - 1)
                continue

        # r     ----|
        # rr    --|
        if r_high > rr_high and rr_high > r_low:
            # r       |--
            # rr    |----
            if r_low > rr_low:
                fresh_ranges[rr] = (rr_low, r_low - 1)
                continue

        # r     --|
        # rr    ----|
        if r_high < rr_high and r_high > rr_low:
            # r     |----
            # rr      |--
            if r_low < rr_high:
                fresh_ranges[rr] = (r_high + 1, rr_high)
                continue

        # r |----|
        # rr     |----|
        if r_high == rr_low and rr_high > r_high:
            fresh_ranges[rr] = (rr_low + 1, rr_high)
            continue

        # r       |----|
        # rr |----|
        if r_low == rr_high and rr_low < r_low:
            fresh_ranges[rr] = (rr_low, rr_high - 1)
            continue

fresh_ranges = [ fr for fr in fresh_ranges if fr != None ]

print(f"\tPart 2: {sum([ high - low + 1 for low, high in fresh_ranges ])}")
