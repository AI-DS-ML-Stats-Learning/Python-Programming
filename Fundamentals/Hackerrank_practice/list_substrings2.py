def wrap(string, max_width):
    chunk = ""
    for i in range(0,len(string), max_width):
        # print(chunk.add(string[i:i+max_width]))
        if i+max_width>len(string):
            chunk = chunk+ string[i:i+max_width] 
        else:
            chunk = chunk + string[i:i+max_width] + "\n"
        # chunk.append("\n")
    return chunk

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)