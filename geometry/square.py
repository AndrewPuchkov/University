def sq_sq(a):
    return a ** 2


def sq_pr(a, b):
    return a * b


def sq_te(b, h):
    return 1 / 2 * b * h


def main():
    print(sq_sq(5))
    print(sq_pr(5, 2))
    print(sq_te(5, 10))


if __name__ == '__main__':
    main()
