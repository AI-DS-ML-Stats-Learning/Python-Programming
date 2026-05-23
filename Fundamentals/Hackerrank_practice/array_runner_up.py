if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr1 = sorted(set(arr))
    print(arr1[-2])
    for _ in arr1:
        print(_)