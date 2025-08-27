import time
import random

print("Bem-vindo ao Jogo de Adivinhação!")
print("Estou pensando em um número entre 1 e 20.")
print("Tente adivinhar qual é. Você tem 5 tentativas.")

numero_secreto = random.randint(1, 20)
tentativas = 5

while tentativas > 0:
    try:
        palpite = int(input("Digite seu palpite: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero_secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")

    tentativas -= 1
    print(f"Tentativas restantes: {tentativas}")
    time.sleep(0.5)

if tentativas == 0:
    print(f"Suas tentativas acabaram. O número era {numero_secreto}.")
