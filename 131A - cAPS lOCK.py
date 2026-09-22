import sys
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    s = data[0]
    if len(s) == 1:
        print(s.swapcase())
    elif s[1:].isupper():
        print(s.swapcase())
    else:
        print(s)
 
if __name__ == "__main__":
    main()
