print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a ilha do tessouro.")
print("Sua missao é achar o tessouro.")

#Write your code below this line 👇

choice1 = input('Voce esta em uma estrada, voce gostaria de ir para aonde? Escreva "esquerda" ou "direita" \n').lower()
if choice1 == "esquerda":
  choice2 = input('Voce chegou a um lago. A uma ilha no meio do lago. Escreva "esperar" para esperar por um barco. Escreva "nadar" para nadar pelo lago ate a ilha. \n').lower()
  if choice2 == "esperar":
    choice3 = input("Voce chegou a ilha ilheso. A uma casa com 3 portas. uma vermelha, uma amarela e uma azul. Qual voce escolhe? \n").lower()
    if choice3 == "vermelha":
      print("A sala estava pegando fogo e voce morreu. Game Over.")
    elif choice3 == "amarela":
      print("Voce achou o tessouro! Voce ganhou!")
    elif choice3 == "azul":
      print("A sala estava cheio de animais famintos. Game Over.")
    else:
      print("voce escolheu uma porta que nao existe. Game Over.")
  else:
    print("Voce foi atacado por peixes famintos. Game Over.")
else:
  print("Voce caiu em um buraco. Game Over.")