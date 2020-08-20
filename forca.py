
def jogar():
    print('**************************')
    print('Bem vindo ao jogo de forca')
    print('**************************')

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    # enquanto não enforcou e não acertou
    while (not enforcou and not acertou):
        chute = input("Entre com o seu chute: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        
        if (erros == 6):
            enforcou = True
        if ('_' not in letras_acertadas):
            acertou = True
        print(letras_acertadas)

            
    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim do jogo!")


if(__name__ == "__main__"):  # Rodado diretamente pelo python (evita rodar ao importar)
    jogar()