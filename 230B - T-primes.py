import sys
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    nums = list(map(int, data[1:]))
    LIMIT = 1000000
    is_prime = [True] * (LIMIT + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(LIMIT**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, LIMIT + 1, i):
                is_prime[j] = False
    t_primes = set()
    for i in range(2, LIMIT + 1):
        if is_prime[i]:
            t_primes.add(i * i)
    out = []
    for x in nums:
        if x in t_primes:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))
 
if __name__ == "__main__":
    main()
