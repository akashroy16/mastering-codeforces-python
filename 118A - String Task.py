import sys

def main():
    s = sys.stdin.read().strip()
    if not s:
        return
    vowels = {'a', 'o', 'y', 'e', 'u', 'i'}
    res = []
    for ch in s.lower():
        if ch not in vowels:
            res.append('.' + ch)
    print(''.join(res))

if __name__ == '__main__':
    main()
