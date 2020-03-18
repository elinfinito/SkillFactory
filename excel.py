    import pandas as pd

    fileLocation = '/Users/mac/Desktop/python/data.xlsx'
    fileName = '/data.xlsx'
    data = pd.ExcelFile(fileLocation + fileName)
    print(data.sheet_names)
    
    #*****
    #xlrd скачан уже
    #Antonio:python mac$ pip3 install xlrd
    #Requirement already satisfied: xlrd in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (1.2.0)
    
    >>>>
    
    Traceback (most recent call last):
  File "/Users/mac/Desktop/python/calc/file_work.py", line 55, in <module>
    data = pd.ExcelFile(fileLocation + fileName)
  File "/Users/mac/Desktop/python/calc/venv/lib/python3.8/site-packages/pandas/io/excel/_base.py", line 821, in __init__
    self._reader = self._engines[engine](self._io)
  File "/Users/mac/Desktop/python/calc/venv/lib/python3.8/site-packages/pandas/io/excel/_xlrd.py", line 20, in __init__
    import_optional_dependency("xlrd", extra=err_msg)
  File "/Users/mac/Desktop/python/calc/venv/lib/python3.8/site-packages/pandas/compat/_optional.py", line 92, in import_optional_dependency
    raise ImportError(msg) from None
ImportError: Missing optional dependency 'xlrd'. Install xlrd >= 1.0.0 for Excel support Use pip or conda to install xlrd.


  >>>>
