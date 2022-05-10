# Program to display the Fibonacci sequence up to n-th term

def fib(nterms):
    n1, n2 = 0, 1  # first two terms
    if nterms >= 0:     # check if nterms is valid
        for i in range(nterms):    # iterate through nterms
            print(n1)       # print n1
            nth = n1 + n2   # finding nth term
            #update values
            n1 = n2
            n2 = nth
    else:
        print("invalid nterm")


fib(2)




