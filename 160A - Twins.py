import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    coins = list(map(int, input_data[1:n+1]))
    
    coins.sort(reverse=True)
    total_sum = sum(coins)
    
    my_sum = 0
    count = 0
    
    for coin in coins:
        my_sum += coin
        count += 1
        if my_sum > total_sum - my_sum:
            break
            
    print(count)

if __name__ == "__main__":
    main()
