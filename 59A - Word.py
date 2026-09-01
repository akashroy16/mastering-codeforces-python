import sys

def main():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    upper_cnt = sum(1 for ch in s if ch.isupper())
    lower_cnt = len(s) - upper_cnt
    
    if upper_cnt > lower_cnt:
        print(s.upper())
    else:
        print(s.lower())

if __name__ == '__main__':
    main()
