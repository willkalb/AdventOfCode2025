from contextlib import chdir


def get_input_line(day):
    with chdir("Inputs\\"):
        with open(str(day), "r") as f:
            return f.read()
        
def get_input_lines(day):
    with chdir("Inputs\\"):
        with open(str(day), "r") as f:
            return [ line.rstrip() for line in f ]