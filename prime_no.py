# Program to check if a number is prime or not
def prime_or_nonprime(n):
    if n > 1:   # prime numbers are greater than 1
        for i in range(2, n):  #checking for factors
            # If n is divisible by any number between 2 and n, it is not prime.
            if n % i == 0:
                print(n, " is not prime")
                break  # break the loop once we find a factor.
        else:
            print(n, " is prime")

    else:
        print(n, "is not prime")


prime_or_nonprime(2)   #call the function
