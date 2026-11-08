import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    pages = [int(x) for x in data[1:8]]
    day = 0
    while n > 0:
        n -= pages[day]
        if n <= 0:
            print(day + 1)
            return
        day = (day + 1) % 7

if __name__ == '__main__':
    solve()
