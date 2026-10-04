import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        s = data[idx+1]
        idx += 2
        
        unique_problems = len(set(s))
        total_balloons = n + unique_problems
        out.append(str(total_balloons))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
