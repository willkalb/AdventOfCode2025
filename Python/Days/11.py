import Helper

DAY = "11"    

devices: dict[str, list[str]] = { l.split(":")[0]: l.split(":")[1][1:].split(" ") for l in Helper.get_input_lines(DAY) }

class Path_Node:
    dac = False
    fft = False

    def __init__(self, _name: str, _children: list[str]):
        self.name = _name
        self.children: list[Path_Node] = []

        for c in _children:
            if c in pathnode_memo.keys():
                self.children.append(pathnode_memo[c])
            else:
                node = Path_Node(c, devices[c] if c != "out" else [])
                pathnode_memo[c] = node
                self.children.append(node)

    def GetPathSpecs(self, depth: int = 0):
        if (self.name, Path_Node.dac, Path_Node.fft, depth) not in pathcount_memo:
            pathcount_memo[(self.name, Path_Node.dac, Path_Node.fft, depth)] = 0

        if self.name == "out":
            pathcount_memo[(self.name, Path_Node.dac, Path_Node.fft, depth)] += 1
            return

        for c in self.children:
            if c.name == "dac":
                Path_Node.dac = True
            elif c.name == "fft":
                Path_Node.fft = True
            
            if (c.name, Path_Node.dac, Path_Node.fft, depth) in pathcount_memo:
                pathcount_memo[(c.name, Path_Node.dac, Path_Node.fft, depth)] *= 2
            else:
                c.GetPathSpecs(depth + 1)

            if c.name == "dac":
                Path_Node.dac = False
            elif c.name == "fft":
                Path_Node.fft = False

pathcount_memo: dict[tuple[str, bool, bool, int], int] = { }
pathnode_memo: dict[str, Path_Node] = {}
you = Path_Node("you", devices["you"])
you.GetPathSpecs()

print(f"\tPart 1: { sum([ v for k, v in pathcount_memo.items() if k[0] == "out" ]) }")


pathcount = 0
pathcount_memo: dict[tuple[str, bool, bool, int], int] = { }
pathnode_memo: dict[str, Path_Node] = {}

svr = Path_Node("svr", devices["svr"])
print(svr.GetPathSpecs())
print(sum([ pathcount_memo[t] for t in pathcount_memo if t[1] and t[2] ] ))

print(f"\tPart 2: { [ (k, v) for k, v in pathcount_memo.items() if k[0] == "out" ]}")


# too low 8388608
# too low 3340484368
# too low 9822536212
# not right 199994565923
