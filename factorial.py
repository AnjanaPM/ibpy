# Python program to find the factorial of a number.
def fact(n):
    p = 1  # initialize a variable p with number 1
    if n >= 0:  # taking all positive numbers
        #take values from 1 to n and multiplying it to p.
        for i in range(1, n + 1):
            p = p * i
        print("factorial of the number is", p)
    else:
        print("invalid input")
fact(3)