print('********************************')
print('Bem vindo ao jogo de adivinhação')
print('********************************')

import random

segredo = random.randint(1,100)  #  gera entre 1 e 100
pontuacao = 1000
tentativas = 0

print("Qual o nível de dificuldade?")
print("1 - Fácil  2 - Médio  3 - Difícil")

nivel = int(input("Defina seu nivel: "))

if(nivel == 1):
    tentativas = 20
elif(nivel == 2):
    tentativas = 10
else:
    tentativas = 5


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
        print('Você acertou e fez {}'.format(pontuacao))
        break
    else:
        maior = chute > segredo
        if(maior):
            print('Você errou! Seu chute foi maior que o número secreto.')
        else:
            print('Você errou! Seu chute foi menor que o número secreto.')
        pontos_perdidos = abs(segredo - chute)
        pontuacao = pontuacao - pontos_perdidos


print('Fim do jogo.')