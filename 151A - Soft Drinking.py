import sys
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n, k, l, c, d, p, nl, np = map(int, data)
    drinks = (k * l) // nl
    limes = c * d
    salt = p // np
    print(min(drinks, limes, salt) // n)
 
if __name__ == "__main__":
    main()
