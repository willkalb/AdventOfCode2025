import importlib

def Exec_Py(day):
    importlib.import_module(f"Python.Days.{day}")
