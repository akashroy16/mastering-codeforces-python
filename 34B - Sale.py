import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    a = [int(x) for x in data[2:2+n]]
    
    a.sort()
    max_earnings = 0
    for i in range(min(m, n)):
        if a[i] < 0:
            max_earnings += -a[i]
        else:
            break
            
    print(max_earnings)

if __name__ == '__main__':
    solve()
