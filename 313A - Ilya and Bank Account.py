import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    
    if n >= 0:
        print(n)
    else:
        s = str(n)
        option1 = int(s[:-1])
        option2 = int(s[:-2] + s[-1])
        print(max(option1, option2))

if __name__ == '__main__':
    solve()
