
def main ():
    i = int(input("Enter the number of fib series you want"))
    current = 0
    next = 1

    if (i == 0 or i == 1):
        print(i)
    else:
        print(current, next, end=" ")
        for j in range(0, i):
            current, next = next, current+next
            print(next, end=" ")


if __name__ == '__main__':
    main ()