import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    b = int(data[1])
    d = int(data[2])
    a = [int(x) for x in data[3:]]
    current = 0
    empties = 0
    for x in a:
        if x <= b:
            current += x
            if current > d:
                empties += 1
                current = 0
    print(empties)

if __name__ == '__main__':
    solve()
