import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    
    time_left = 240 - k
    ans = 0
    
    for i in range(1, n + 1):
        if time_left >= 5 * i:
            time_left -= 5 * i
            ans += 1
        else:
            break
            
    print(ans)

if __name__ == '__main__':
    solve()
