import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    
    mapping = {}
    idx = 2
    for _ in range(m):
        w1 = data[idx]
        w2 = data[idx+1]
        mapping[w1] = w2 if len(w2) < len(w1) else w1
        idx += 2
        
    lecture = data[idx:idx+n]
    res = [mapping[w] for w in lecture]
    print(" ".join(res))

if __name__ == '__main__':
    solve()
