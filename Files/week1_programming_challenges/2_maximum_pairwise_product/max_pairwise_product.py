def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


input_numbers = [7, 5, 14, 2, 8, 8, 10, 1, 2, 3,]

def max_pairwise_productFast(numbers):
    sortedNumbers = sorted(numbers, reverse=True) # time complexity of n log n. Uses Timsort algorthim. Hybrid sort method (binInsert + MergeSort)
    index1 = 0
    index2 = 1
    maxprod = sortedNumbers[index1] * sortedNumbers[index2]
    return maxprod
    

if __name__ == '__main__':
    # _ = int(input())
    # input_numbers = list(map(int, input().split()))
    print(max_pairwise_productFast(input_numbers))
