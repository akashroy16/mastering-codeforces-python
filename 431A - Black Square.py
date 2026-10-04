import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    a = [int(x) for x in data[:4]]
    s = data[4]
    
    calories = sum(a[int(ch) - 1] for ch in s)
    print(calories)

if __name__ == '__main__':
    solve()
