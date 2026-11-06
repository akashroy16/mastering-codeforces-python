import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    count_q = 0
    qa = 0
    qaq = 0
    for ch in s:
        if ch == 'Q':
            qaq += qa
            count_q += 1
        elif ch == 'A':
            qa += count_q
    print(qaq)

if __name__ == '__main__':
    solve()
