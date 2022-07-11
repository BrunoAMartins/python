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

escolha = int(input("Qual voce escolhe? Escrava 0 para pedra, 1 para papel ou 2 para tessoura.\n"))
print(game_imagens[escolha])

cp_escolha = random.randint(0, 2)
print("Escolha do computador:")
print(game_imagens[cp_escolha])

if escolha >= 3 or escolha < 0: 
  print("voce digitou um numeor invalido, Voce perdeu!") 
elif escolha == 0 and cp_escolha == 2:
  print("Voce ganhou!")
elif cp_escolha == 0 and escolha == 2:
  print("Voce perdeu")
elif cp_escolha > escolha:
  print("Voce perdeu")
elif escolha > cp_escolha:
  print("Voce ganhou")
elif cp_escolha == escolha:
  print("E um empate")

