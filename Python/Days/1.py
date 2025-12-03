import Helper
DAY = "1"

lines = Helper.get_input_lines(DAY)

num = 50
zero_counter = 0
for instr in lines:
    if instr[0].lower() == "r":
        num = num + int(instr[1:])
        while num > 99:
            num = num - 100
    elif instr[0].lower() == "l":
        num = num - int(instr[1:])
        while num < 0:
            num = num + 100
    
    if num == 0:
        zero_counter = zero_counter + 1

print(f"\tPart 1: {zero_counter}")


num = 50
zero_counter = 0
for instr in lines:
    if instr[0].lower() == "r":
        clicks = int(instr[1:])
        for c in range(clicks):
            num = num + 1
            if num == 100:
                num = 0
            if num == 0:
                zero_counter = zero_counter + 1
    elif instr[0].lower() == "l":
        clicks = int(instr[1:])
        for c in range(clicks):
            num = num - 1
            if num == -1:
                num = 99
            if num == 0:
                zero_counter = zero_counter + 1
    
print(f"\tPart 2: {zero_counter}")
