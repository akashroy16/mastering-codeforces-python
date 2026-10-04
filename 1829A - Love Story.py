import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    target = "codeforces"
    out = []
    
    for i in range(1, t + 1):
        s = data[i]
        diff = sum(1 for a, b in zip(s, target) if a != b)
        out.append(str(diff))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
