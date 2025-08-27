def forca():
    palavra = "python"
    letras_adivinhadas = []
    tentativas = 6
    
    # Desenhos da forca para cada estado (de 6 tentativas até 0)
    estagios = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |   
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |   
           |
        """
    ]
    
    print("Bem-vindo ao Jogo da Forca!")
    print(f"A palavra tem {len(palavra)} letras.")
    
    while tentativas > 0:
        print(estagios[tentativas])
        
        display = ""
        for letra in palavra:
            if letra in letras_adivinhadas:
                display += letra + " "
            else:
                display += "_ "
        print("\nPalavra:", display.strip())
        
        tentativa = input("Digite uma letra: ").lower()
        
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue
        
        if tentativa in letras_adivinhadas:
            print("Você já tentou essa letra.")
            continue
        
        if tentativa in palavra:
            letras_adivinhadas.append(tentativa)
            print("Acertou!")
        else:
            tentativas -= 1
            print(f"Letra errada! Tentativas restantes: {tentativas}")
        
        if all(letra in letras_adivinhadas for letra in palavra):
            print(f"Parabéns! Você ganhou! A palavra era '{palavra}'.")
            break
    else:
        print(estagios[0])
        print(f"Fim do jogo! Você perdeu. A palavra era '{palavra}'.")
        
forca()
