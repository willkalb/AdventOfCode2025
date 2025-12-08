import Helper
DAY = "2"

line = Helper.get_input_line(DAY)
ranges = line.split(",")

# { id_len: [ (groups, group_len) ]}
divs: dict[int, list[tuple[int, int]]] = {
    10: [ (2, 5) ],
    8: [ (2, 4) ],
    6: [ (2, 3) ],
    4: [ (2, 2) ],
    2: [ (2, 1) ]
}

ids_sum = 0
for r in ranges:
    i_first, i_last = int(r[:r.index("-")]), int(r[r.index("-") + 1:])

    for id in range(i_first, i_last + 1):
        str_id = str(id)
        len_id = len(str_id)

        if len_id not in divs.keys():
            continue
        
        opts = divs[len_id]
        for opt in opts:
            if str_id[:opt[1]] * opt[0] == str_id:
                ids_sum += id
                break

print(f"\tPart 1: {ids_sum}")

divs = {
    10: [ (10, 1), (5, 2), (2, 5) ],
    9: [ (9, 1), (3, 3) ],
    8: [ (8, 1), (4, 2), (2, 4)],
    7: [ (7, 1) ],
    6: [ (6, 1), (3, 2), (2, 3)],
    5: [ (5, 1) ],
    4: [ (4, 1), (2, 2)],
    3: [ (3, 1) ],
    2: [ (2, 1) ],
    1: [ ]
}

ids_sum = 0
for r in ranges:
    i_first, i_last = int(r[:r.index("-")]), int(r[r.index("-") + 1:])

    for id in range(i_first, i_last + 1):
        str_id = str(id)
        len_id = len(str_id)
        
        opts = divs[len_id]
        for opt in opts:
            if str_id[:opt[1]] * opt[0] == str_id:
                ids_sum += id
                break

print(f"\tPart 2: {ids_sum}")
