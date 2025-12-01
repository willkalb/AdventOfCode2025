from .db_connect import Open, Close
from Helper import *

def Exec_SQL(day):
    db = Open()

    db.execute(f"exec Day{day} @input_as_string = ?, @part = ?", [ ",".join(get_input_lines(day)), 1 ])
    print("\tPart 1: ", db.fetchval())

    db.execute(f"exec Day{day} @input_as_string = ?, @part = ?", [ ",".join(get_input_lines(day)), 2 ])
    print("\tPart 2: ", db.fetchval())

    Close()
