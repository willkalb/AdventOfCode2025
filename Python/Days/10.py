import Helper

DAY = "10"


def GetScore(_mach_final: str, _mach_curr: str, _buttons: list[list[int]]) -> int:
    score: int = 0
    button_presses: int = 0

    # list of (machine state, score, button presses)
    q: list[tuple[str, int, int]] = [ (_mach_curr, score, button_presses) ]

    ii = 0

    while True:
        ii += 1

        _mach_curr, score, button_presses = q[0]

        if _mach_curr == _mach_final:
            print(f"\t {button_presses}")
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

    


mach_specs = [ (
    l[l.find("[") + 1:l.find("]")],
    [ list(map(int, b.replace("(", "").replace(")", "").split(","))) for b in l[l.find("]") + 2:l.find("{") - 1].split(" ") ],
    list(map(int, l[l.find("{") + 1:l.find("}")].split(",")))
) for l in Helper.get_input_lines(DAY) ]

button_sum = 0
for ms in mach_specs:
    mach = "." * len(ms[0])

    button_sum += GetScore(ms[0], mach, ms[1])

print(f"\tPart 1: {button_sum}")


for i in range(0, len(mach_specs)):
    pass

print(f"\tPart 2: {0}")
