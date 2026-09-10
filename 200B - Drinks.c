import sys
 
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    percentages = list(map(int, input_data[1:n+1]))
    
    print(sum(percentages) / n)
 
if __name__ == "__main__":
    main()
