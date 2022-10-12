import random
a= random.randint(1,9)
count = 0
while True:
    n = int(input("Enter a guess: "))
    count += 1
    if n==a:
        print(f"You have Guessed in {count} attempt")
        break
    else:
        print("wrong guess,try again!")
