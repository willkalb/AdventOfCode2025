import Helper
DAY = "3"

banks = Helper.get_input_lines(DAY)

joltage_sum = 0
for bank in banks:
    high_first, high_first_pos = 0, -1
    for x in range(0, len(bank) - 1):
        i_first = int(bank[x:x + 1])
        high_first, high_first_pos = (i_first, x) if i_first > high_first else (high_first, high_first_pos)

    high_second, high_second_pos = 0, -1
    for x in range(1, len(bank)):
        if x <= high_first_pos:
            continue

        i_second = int(bank[x:x + 1])
        high_second, high_second_pos = (i_second, x) if i_second > high_second else (high_second, high_second_pos)

    joltage_sum += int(str(high_first) + str(high_second))
        

print(f"\tPart 1: {joltage_sum}")

joltage_sum = 0
for bank in banks:
    high_first, high_first_pos = 0, -1
    highs, poss = [0] * 12, [-1] * 12
    
    for i in range(12):
        start =  12 - 12 + i
        end = len(bank) - 12 + i
        for ii in range(start, end + 1):
            if ii <= max(poss):
                continue
            highs[i], poss[i] = (int(bank[ii]), ii) if int(bank[ii]) > highs[i] else (highs[i], poss[i])

    joltage_sum += int("".join([ str(i) for i in highs ]))

print(f"\tPart 2: {joltage_sum}")
