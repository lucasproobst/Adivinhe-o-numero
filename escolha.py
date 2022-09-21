import random
import os

print('******** Seja bem-vindo(a) ao jogo da adivinhação. ********\n')
print('[F] Fácil (0 a 10) \n')
print('[M] Médio (0 a 30) \n')
print('[D] Dificil (0 a 100) \n')
print('[E] Extremo (0 a 1000) \n')

escolha = input('Escolha: ')

os.system('clear')

dificultade_F = random.randint(0, 10)
dificultade_M = random.randint(0, 30)
dificultade_D = random.randint(0, 100)
dificultade_E = random.randint(0, 1000)

acertou = False
tentativas = 0

# print(dificultade_F)
# print(dificultade_M)
# print(dificultade_D)
# print(dificultade_E)

while not acertou:
    jogador = int(input('Número: '))

    if escolha == 'F' or escolha == 'f' and jogador == dificultade_F:
        acertou = True
    elif escolha == 'M' or escolha == 'm' and jogador == dificultade_M:
        acertou = True
    elif escolha == 'D' or escolha == 'd' and jogador == dificultade_D:
        acertou = True
    elif escolha == 'E' or escolha == 'e' and jogador == dificultade_E:
        acertou = True
    tentativas += 1

os.system('clear')

print(f'Parabéns! Voce acertou com {tentativas} tentativas.')
