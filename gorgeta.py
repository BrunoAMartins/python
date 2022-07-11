
print("bem vindo ao calculador de gorgeta!")
conta = float(input("quanto foi a conta total? $"))
gorgeta = int(input("qual a procentagem de gorgeta gostaria de dar? 10, 12, or 15? "))
num_pessoas = int(input("em quantas pessoas vao ser divida a conta?"))

porc_gorgeta= gorgeta / 100
total_gorgeta = conta * porc_gorgeta
total_conta = conta + total_gorgeta
conta_p_pessoa = total_conta / num_pessoas
total_f = round(conta_p_pessoa, 2)


print(f"Cada pessoa vai pagar: ${total_f}")