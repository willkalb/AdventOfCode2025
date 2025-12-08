import Helper
DAY = "4"

rows = Helper.get_input_lines(DAY)

ROWS = len(rows)
COLS = len(rows[0])

accessable: list[tuple[int, int]] = []
for r in range(ROWS):
    for c in range(COLS):
        if rows[r][c] != "@":
            continue

        paper_neighbors: list[tuple[int, int]] = []
        for r_offset in range(-1, 2):
            for c_offset in range(-1, 2):
                if r_offset == 0 and c_offset == 0:
                    continue
                new_r = r + r_offset
                if new_r < 0 or new_r > ROWS - 1:
                    continue
                new_c = c + c_offset
                if new_c < 0 or new_c > COLS - 1:
                    continue
                if rows[new_r][new_c] == "@":
                    paper_neighbors.append((new_r, new_c))

        if len(paper_neighbors) < 4:
            accessable.append((r, c))        

print(f"\tPart 1: {len(accessable)}")


removed: list[tuple[int, int]] = []
while True:
    gen_removed: list[tuple[int, int]] = []
    for r in range(ROWS):
        for c in range(COLS):
            if rows[r][c] != "@":
                continue

            paper_neighbors = []
            for r_offset in range(-1, 2):
                for c_offset in range(-1, 2):
                    if r_offset == 0 and c_offset == 0:
                        continue
                    new_r = r + r_offset
                    if new_r < 0 or new_r > ROWS - 1:
                        continue
                    new_c = c + c_offset
                    if new_c < 0 or new_c > COLS - 1:
                        continue
                    if rows[new_r][new_c] == "@":
                        paper_neighbors.append((new_r, new_c))

            if len(paper_neighbors) < 4:
                gen_removed.append((r, c)) 
    
    if len(gen_removed) == 0:
        break

    for r, c in gen_removed:
        rows[r] = rows[r][:c] + "." + rows[r][c + 1:]
        removed.append((r, c))

print(f"\tPart 2: {len(removed)}")
