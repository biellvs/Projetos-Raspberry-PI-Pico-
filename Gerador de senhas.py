import random

def shuffle_list(lst):
    # Embaralha a lista in-place
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]

def gerar_senha(tamanho=12):
    letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    simbolos = "!@#$%^&*()-_+=<>?"

    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos

    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    senha += [random.choice(todos_caracteres) for _ in range(tamanho - 4)]

    shuffle_list(senha)

    return "".join(senha)

print("Gerador de Senhas")
while True:
    try:
        tamanho = int(input("Digite o tamanho da senha (mínimo 4): "))
        if tamanho < 4:
            print("Tamanho mínimo é 4.")
            continue
    except ValueError:
        print("Digite um número válido.")
        continue
    
    senha = gerar_senha(tamanho)
    print("Senha gerada:", senha)

    opcao = input("Quer gerar outra senha? (s/n): ").lower()
    if opcao != 's':
        print("Obrigado por usar o gerador de senhas!")
        break
