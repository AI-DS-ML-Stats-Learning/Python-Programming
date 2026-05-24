cube = lambda x: pow(x,3)

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = []
    a = 0
    b = 1
    c = a+b
    if n >=1:
        fib.append(a)
        if n >= 2:
            fib.append(b)
        if n >=3:
            fib.append(c)
        if n >=4:
            for i in range (n-3):
                a = b
                b = c
                c = a+b
                fib.append(c)
    # print(fib)
    return(fib)
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))