import importlib

def Exec_Py(day: int):
    importlib.import_module(f"Python.Days.{day}")
