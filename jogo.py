
print("********************************")
print("Bem vendo ao jogo de Adivinhação!")
print("********************************")


numero_secreto = 42

chute = input("Digite o seu número: ")

print("Você digitou: ", chute)

if numero_secreto == chute:
    print("Você acertou")
else:
    print("Você errou")