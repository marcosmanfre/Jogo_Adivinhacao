import forca
import jogo

print("********************************")
print("******Escolha o seu jogo!*******")
print("********************************")

print("(1) Forca (2) Adivinhação")

jogito = int(input("Qual jogo?"))

if(jogito == 1):
    print("Jogando Forca")
    forca.jogar()
elif(jogito == 2):
    print("Jogando Adivinhação")
    jogo.jogar()
