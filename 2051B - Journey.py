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
        a = int(data[idx+1])
        b = int(data[idx+2])
        c = int(data[idx+3])
        idx += 4
        
        cycle_sum = a + b + c
        full_cycles = n // cycle_sum
        rem = n % cycle_sum
        
        days = full_cycles * 3
        if rem > 0:
            rem -= a
            days += 1
        if rem > 0:
            rem -= b
            days += 1
        if rem > 0:
            days += 1
        out.append(str(days))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
