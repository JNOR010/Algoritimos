secreto = 'Maguinho'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print('Voce perde !!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso nao vale, digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhull, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Aff, a letra "{letra}" Nao existe na palavra secreta')
        digitadas.pop()


    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, voce Ganhou !!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta esta assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Voce ainda tem {chances} chances.')
    print()