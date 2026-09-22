import sys
 
def main():
    s = sys.stdin.read().split()
    if s:
        print(" ".join(s[0].replace("WUB", " ").split()))
 
if __name__ == "__main__":
    main()
