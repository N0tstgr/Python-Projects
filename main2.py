import random
n = random.randint(1, 100)
a = -1
guesses = 0
while( a !=n):
   
    a = int(input("Guess the number : "))
    if(a>n):
        print("Lower numbe please")
    elif(a<n):
        print("Higher number please")
    guesses +=1

print(f"You have guessed the {n} correctly in {guesses} attempt ")