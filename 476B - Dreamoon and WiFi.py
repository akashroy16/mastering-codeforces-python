import sys
import math

def solve():
    lines = sys.stdin.read().split()
    if not lines:
        return
    s1 = lines[0]
    s2 = lines[1]
    
    target = s1.count('+') - s1.count('-')
    curr = s2.count('+') - s2.count('-')
    q_count = s2.count('?')
    
    needed = target - curr
    if (needed + q_count) % 2 != 0 or abs(needed) > q_count:
        print("0.000000000000")
        return
        
    plus_needed = (needed + q_count) // 2
    ways = math.comb(q_count, plus_needed)
    total_ways = 1 << q_count
    
    ans = ways / total_ways
    print(f"{ans:.12f}")

if __name__ == '__main__':
    solve()
