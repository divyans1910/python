def primecheck(number):
    prime=True
    for i in range(2,number-1):
        if number%i==0:
            prime=False
    if prime:
            print("It is Prime")
    else:
            print("It is Not Prime")

number=int(input("Enter the number: "))
primecheck(number)
