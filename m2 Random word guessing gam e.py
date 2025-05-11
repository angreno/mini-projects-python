import random

#taking username as input
user_name =input("please type your name : ")
#word library
word = ['eye' , 'hand' , 'kunal' , 'mummy' , 'aryan']
#selecting one word
result = random.choice(word)


print(f"hey {user_name} \n welcome to the word arena" , sep='*')

print("please choose your word from " , word[:])
for i in range(5):
    user_guess = input("your guess ->")
    if(result == user_guess):
        print("you won the word was ",result)
    i=i+1



