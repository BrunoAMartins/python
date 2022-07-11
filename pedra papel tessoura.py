import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tessoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_imagens = [pedra, papel, tessoura]

escolha = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_imagens[escolha])

cp_escolha = random.randint(0, 2)
print("Computer chose:")
print(game_imagens[cp_escolha])

if escolha >= 3 or escolha < 0: 
  print("You typed an invalid number, you lose!") 
elif escolha == 0 and cp_escolha == 2:
  print("You win!")
elif cp_escolha == 0 and escolha == 2:
  print("You lose")
elif cp_escolha > escolha:
  print("You lose")
elif escolha > cp_escolha:
  print("You win!")
elif cp_escolha == escolha:
  print("It's a draw")

