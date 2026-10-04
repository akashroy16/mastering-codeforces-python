import sys

def solve():
    sequence = []
    i = 1
    while len(sequence) < 1000:
        if i % 3 != 0 and i % 10 != 3:
            sequence.append(i)
        i += 1

    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = [str(sequence[int(data[j]) - 1]) for j in range(1, t + 1)]
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
