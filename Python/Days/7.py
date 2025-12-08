import Helper
DAY = "7"

lines = Helper.get_input_lines(DAY) 

def SetPathSpecs(path: list[tuple[int, int]]):
    global paths_ended
    start_path_num = paths_ended

    x, y = path[-1]
    if y >= len(lines):
        paths_ended += 1
        return
    
    if (x, y) in path_memo:
        paths_ended += path_memo[(x, y)]
        return
    
    if (lines[y][x] == "^"):
        splits.add((x, y))

        path.append((x - 1, y + 1))
        SetPathSpecs(path)
        path.pop()

        path.append((x + 1, y + 1))
        SetPathSpecs(path)
        path.pop()
    else:
        path.append((x, y + 1))
        SetPathSpecs(path)
        path.pop()

    path_memo[(x, y)] = paths_ended - start_path_num


path_memo = {}
splits = set()
paths_ended = 0
SetPathSpecs([(lines[0].find("S"), 0)])

print(f"\tPart 1: {len(splits)}")
print(f"\tPart 2: {paths_ended}")