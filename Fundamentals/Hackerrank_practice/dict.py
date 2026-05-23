if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # scores = {}
    # scores = {name:score for name, score in student_marks.items() if name ==query_name}
    s = 0
    for i in student_marks[query_name]:
        s = s+i
    
    print(f"{s/3:.2f}")