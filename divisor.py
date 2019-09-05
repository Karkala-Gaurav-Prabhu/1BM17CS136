def divisor(num):
    for i in range(1, num+1):
        if num%i == 0:
            print(i)

num = int(input("Enter Number to find Divisors: "))
print("The Divisors of ", str(num), "are: ")
divisor(num)
