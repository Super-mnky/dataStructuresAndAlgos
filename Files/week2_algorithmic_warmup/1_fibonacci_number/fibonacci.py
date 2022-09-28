def fibRecurse(n):
    if n <= 1:
        return n

    return fibRecurse(n - 1) + fibRecurse(n - 2)

def fibRecurs_fast(n):
    pass


if __name__ == '__main__':
    input_n = int(input())
    print(fibRecurse(input_n))
