from Python import Exec_Py
from SQL import Exec_SQL

run_days: list[dict[str, int | bool]] = [
    {
        "day": 1,
        "python": False,
        "sql": False
    },
    {
        "day": 2,
        "python": False,
        "sql": False
    },
    {
        "day": 3,
        "python": False,
        "sql": False
    },
    {
        "day": 4,
        "python": False,
        "sql": False
    },
    {
        "day": 5,
        "python": False,
        "sql": False
    },
    {
        "day": 6,
        "python": False,
        "sql": False
    },
    {
        "day": 7,
        "python": False,
        "sql": False
    },
    {
        "day": 8,
        "python": False,
        "sql": False
    },
    {
        "day": 9,
        "python": False,
        "sql": False
    },
    {
        "day": 10,
        "python": True,
        "sql": False
    }
]

for spec in [ s for s in run_days if s["python"] or s["sql"] ]:
    print(f"Day {spec["day"]}:")

    if spec["python"]:
        print("\tPython:".expandtabs(4))
        Exec_Py(spec["day"])
    
    if spec["sql"]:
        print("\tSQL:".expandtabs(4))
        Exec_SQL(spec["day"])
