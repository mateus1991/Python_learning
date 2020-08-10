print('********************************')
print('Bem vindo ao jogo de adivinhação')
print('********************************')

segredo = 42
tentativas = 3


for rodada in range(1,tentativas + 1):
    print ("Tentativa {} de {}".format(rodada, tentativas))
    chute_str = input('Entre com o seu chute (Entre 1 e 100)')
    print('Você digitou ',chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acerto = segredo == chute

    if(acerto):
        print('Você acertou!')
        break
    else:
        maior = chute > segredo
        if(maior):
            print('Você errou! Seu chute foi maior que o número secreto.')
        else:
            print('Você errou! Seu chute foi menor que o número secreto.')


print('Fim do jogo.')