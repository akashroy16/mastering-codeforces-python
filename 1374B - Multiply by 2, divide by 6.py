import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        cnt2 = 0
        cnt3 = 0
        
        while n % 2 == 0:
            cnt2 += 1
            n //= 2
            
        while n % 3 == 0:
            cnt3 += 1
            n //= 3
            
        if n == 1 and cnt2 <= cnt3:
            moves = (cnt3 - cnt2) + cnt3
            out.append(str(moves))
        else:
            out.append("-1")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
