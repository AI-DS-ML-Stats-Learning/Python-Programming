import os

with open("log.bin", "rb") as file:
    print(file.seek(os.SEEK_CUR))
    print(file.seek(os.SEEK_SET))
    print(file.seek(os.SEEK_END))
    print(file.seek(-4, os.SEEK_END))