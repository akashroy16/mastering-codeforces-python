import sys
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    a, b, c = data[0], data[1], data[2]
    print("YES" if sorted(a + b) == sorted(c) else "NO")
 
if __name__ == "__main__":
    main()
