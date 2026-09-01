import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    s, t = data[0], data[1]
    
    if s == t[::-1]:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
