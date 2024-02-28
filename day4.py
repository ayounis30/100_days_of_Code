rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice = int(input("Choose from the following, 0 for rock, 1 for paper, 2 for scissors: " ))

##while choice > 2 or choice < 0 :
 ## break
##print("You have entered an invalid number! ")


random_choice = random.randint(0, 2)
ascii_image = [rock, paper, scissors]
print(f"You are {choice}")
print(ascii_image[choice])
print(f"Computer is {random_choice}")
print(ascii_image[random_choice])

if choice > 2 or choice < 0 :
  print("You have cpentered an invalid number! ")
elif choice == 0 and random_choice == 2:
    print("User wins, rock beats scissors ")
elif choice == 0 and random_choice == 1:
    print("You lose, paper beats rock")
elif choice == random_choice :
    print("Tie Game!")
elif choice == 1 and random_choice == 0 :
    print("You win, paper beats rock")
elif choice == 1 and random_choice == 2 :
    print("You Lose, scissors beats paper")
elif choice == 2 and random_choice == 0 :
    print("You lose, rock beats scissor")
elif choice == 2 and random_choice == 1 :
    print(" You win, scissor beats paper")
