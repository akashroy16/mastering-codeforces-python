import sys
 
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    p = list(map(int, input_data[1:n+1]))
    
    ans = [0] * n
    for i in range(n):
        ans[p[i] - 1] = i + 1
        
    print(*(ans))
 
if __name__ == "__main__":
    main()
