import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    b = int(data[1])
    d = int(data[2])
    a = [int(x) for x in data[3:3+n]]
    
    current_sum = 0
    emptied = 0
    for x in a:
        if x <= b:
            current_sum += x
            if current_sum > d:
                emptied += 1
                current_sum = 0
    print(emptied)

if __name__ == '__main__':
    solve()
