number = 7
prime = True

for i in range(2, number-1):
    if number % i == 0:
        print("is not prime")
        break
else:
    print("is prime")