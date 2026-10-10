import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    curr = 'a'
    moves = 0
    for ch in s:
        diff = abs(ord(ch) - ord(curr))
        moves += min(diff, 26 - diff)
        curr = ch
    print(moves)

if __name__ == '__main__':
    solve()
