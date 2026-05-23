def merge_the_tools(string, k):
    # your code goes here
    l = len(string)
    chunk = []
    for i in range(0,l,k):
        chunk = string[i:i+k]
        print("".join(list(dict.fromkeys(chunk))))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)