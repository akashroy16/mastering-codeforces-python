import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n, k = int(input_data[0]), int(input_data[1])
    scores = [int(x) for x in input_data[2:2 + n]]
    
    k_score = scores[k - 1]
    advancers = sum(1 for score in scores if score >= k_score and score > 0)
    
    print(advancers)

if __name__ == '__main__':
    main()
