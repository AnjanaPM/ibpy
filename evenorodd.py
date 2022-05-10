def evenorodd(n):  # defining even or odd function

    if n == 0:
        print("0 is neither even nor odd")
    elif n % 2 == 0:  # if the number is divisible by 2,the number is even.
        print(n, " is even ")
    else:                # if the number is not divisible by 2,the number is odd.
        print(n, "is odd")


evenorodd(5)
