import Helper

DAY = "10"


def GetButtonPresses_1(_mach_final: str, _mach_curr: str, _buttons: list[list[int]]) -> int:
    score: int = 0
    button_presses: int = 0

    # list of (machine state, score, button presses)
    q: list[tuple[str, int, int]] = [ (_mach_curr, score, button_presses) ]

    while True:
        _mach_curr, score, button_presses = q[0]

        if _mach_curr == _mach_final:
            return button_presses

        q = q[1:]

        for _b in _buttons:
            _next_mach_state = _mach_curr

            for _i in _b:
                pre = _next_mach_state[:_i] 
                post =_next_mach_state[_i + 1:]

                _next_mach_state = pre + ("." if _next_mach_state[_i] == "#" else "#") + post

            local_score = 0
            for i in range(len(_mach_final)):
                if _mach_final[i] == _next_mach_state[i]:
                    local_score += 1
                
            if _next_mach_state in [ t[0] for t in q ]:
                if _next_mach_state in [ t[0] for t in q if _next_mach_state == t[0] and score + local_score < t[1] and button_presses + 1 < t[2] ]:
                    q.append((_next_mach_state, score + local_score, button_presses + 1))
            else:
                q.append((_next_mach_state, score + local_score, button_presses + 1))
    
        q = sorted(q, key=lambda x: (x[2], -x[1]))

def GetButtonPresses_2(_joltage_final: tuple[int, ...], _joltage_curr: tuple[int, ...], _buttons: list[list[int]]) -> int:
    total: int = sum(_joltage_final)
    button_presses: int = 0

    # list of (machine state, score, button presses)
    q: list[tuple[tuple[int, ...], int, int]] = [ (_joltage_curr, 0, button_presses) ]

    ii = 0
    print(_joltage_final)
    while True:
        ii += 1
        _joltage_curr, score, button_presses = q[0]

        if _joltage_curr == _joltage_final:
            return button_presses

        if ii % 1000 == 0:
            print(f"\t {ii}", len(q), (_joltage_curr, score, button_presses))

        q = q[1:]

        for _b in _buttons:
            _next_joltage_state = _joltage_curr

            for _i in _b:
                pre = _next_joltage_state[:_i] 
                post =_next_joltage_state[_i + 1:]

                _next_joltage_state = (*pre, _next_joltage_state[_i] + 1, *post)
            
            # over = False
            local_total: int = sum(_joltage_curr)
            if local_total > total:
                continue

            over = False
            for i in range(len(_joltage_final)):
                if _next_joltage_state[i] > _joltage_final[i]:
                    over = True
                    break
            
            if over:
                continue

            
            # if _next_joltage_state in [ t[0] for t in q if t[0] == _next_joltage_state and t[2] < button_presses + 1 ]:
            #     continue

            q.append((_next_joltage_state, local_total, button_presses + 1))

            #q = [ t for t in q if (t[0] == _next_joltage_state and t[2] <= button_presses + 1) or t[0] != _next_joltage_state ]
    
        q = sorted(q, key=lambda x: (x[2], -x[1]))

    


mach_specs = [ (
    l[l.find("[") + 1:l.find("]")],
    [ list(map(int, b.replace("(", "").replace(")", "").split(","))) for b in l[l.find("]") + 2:l.find("{") - 1].split(" ") ],
    list(map(int, l[l.find("{") + 1:l.find("}")].split(",")))
) for l in Helper.get_input_lines(DAY) ]

button_sum = 0
for ms in mach_specs:
    mach = "." * len(ms[0])

    button_sum += GetButtonPresses_1(ms[0], mach, ms[1])

print(f"\tPart 1: {button_sum}")


button_sum = 0
for ms in mach_specs:
    joltage = tuple([ 0 for _ in range(len(ms[2])) ])

    # Get "least common factor".
    # Determine least amount of button presses so that they all equal the same number again.
    

    button_sum += GetButtonPresses_2(tuple(ms[2]), joltage, ms[1])

print(f"\tPart 2: {button_sum}")
