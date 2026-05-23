def split_and_join(line):
    split_r = list(line.split(", "))
    
    return "".join(split_r)
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)