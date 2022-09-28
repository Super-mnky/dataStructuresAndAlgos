import time
import time


def fibRecurs(n):
    # base case check
    if n in {0, 1}:
        return n

    # if not 0 or 1, computer n-1 and n-2
    else:
        return fibRecurs(n - 1) + fibRecurs(n - 2)


# Time Comeplexity:     O(2^n)
# Auxiliary Space:      O(n)
def fibRecurs_Fast(n, cache={0: 0, 1: 1}):  # pass in n and starting/latest version of cache w/ base cases defined

    # check if we already computed n, if so return n
    if n in cache:
        return cache.get(n)

    # if not, compute and store, then return
    cache[n] = fibRecurs_Fast(n - 1) + fibRecurs_Fast(n - 2)
    return cache.get(n)


# Time Comeplexity:     O(n)
# Auxiliary Space:      O(n)


if __name__ == '__main__':
    input_n = int(input())

    start = time.time()
    ans = fibRecurs(input_n)
    stop = time.time()
    print("\nThe answer is: ", ans, "\nWhich took: ", (stop - start), "using the slow method.")

    start = time.time()
    ans = fibRecurs_Fast(input_n)
    stop = time.time()
    print("\nThe answer is: ", ans, "\nWhich took: ", (stop - start), "using the fast method.")

