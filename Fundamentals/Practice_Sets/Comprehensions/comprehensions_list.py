
filenames = ["main.py", "helper.txt", "data.json", "utils.py", "script.PY"]

'''THis we have used regex but we have inbuilt string functions that are faster than this'''
# import re
# list1 = [str.upper(i) for i in filenames if re.search(r'\.py$', i, re.IGNORECASE)]
# print(list1)

list1 = [i.upper() for i in filenames if i.lower().endswith(".py")]
print(list1)