from .db_connect import Open, Close

def Exec_SQL(day):
    db = Open()

    db.execute(f"exec Day{day} @input_as_string = ?, @part = ?", [ "abc,def", 1 ])
    print("\tPart 1: ", db.fetchval())

    db.execute(f"exec Day{day} @input_as_string = ?, @part = ?", [ "ghi,jkl", 2 ])
    print("\tPart 2: ", db.fetchval())

    Close()
