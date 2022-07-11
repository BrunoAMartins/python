#Password Generator Project
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao gerador de senha!")
n_letras = int(input("Quantas letras voce gostaria de ter na sua senha?\n")) 
n_simbolos = int(input(f"E simbolos?\n"))
n_numeros = int(input(f"E qauntos numeros?\n"))

senha_L = []

for i in range(1, n_letras + 1):
  senha_L.append(random.choice(letras))

for i in range(1, n_simbolos + 1):
  senha_L += random.choice(simbolos)

for i in range(1, n_numeros + 1):
  senha_L += random.choice(numeros)

#print(senha_L)
random.shuffle(senha_L)
#print(senha_L)

senha = ""
for i in senha_L:
  senha += i

print(f"Your password is: {senha}")