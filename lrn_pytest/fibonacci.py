def get_fib_list(n):
    n1 = 0
    n2 = 1
    fib_list = []
    if n <= 0:
        raise ValueError()
    for i in range(1, n+1):
        if i < 3:
            fib_list.append(i - 1)
        else:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            fib_list.append(nth)
    return fib_list


if __name__ == '__main__':
    print(get_fib_list(0))
