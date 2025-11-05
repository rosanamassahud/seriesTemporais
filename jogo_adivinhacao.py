print('------------------------------------------------')
print('------- Bem vindo ao jogo de adivinhação -------')
print('------------------------------------------------')
numero_secreto = 45

chute = int(input('Adivinha o número (inteiro): '))

# teste do chute
if (chute == numero_secreto):
    print('Você acertou!')
    print('Parabéns!')
else:
    print('Você errou!')    
    if (chute > numero_secreto):
        print('Você chutou um número MAIOR que o número secreto')
    elif (chute < numero_secreto):
        print('Você chutou um número MENOR que o número secreto')
    print('Tente novamente')

print('Fim do jogo')