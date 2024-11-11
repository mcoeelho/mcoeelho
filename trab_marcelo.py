import random
escala = int(input('Escolha o tamanho da escala do game: '))

functions = ['w','a','s','d']
frases = ['Quem se mexer é gay', "Mexe ai bichona", 'Anda logo', 'Bora rapaz']
mortes = ['Se matou lerdão!', 'Caiu otário!', 'You fell bitch!', 'MAS É BURRO!', 'pqp tu não leu a única regra?!?!']
fim=random.choice(mortes)
h=0
v=0

while True:
    if h <0 or v <0:
        break
    if h >= escala or v >= escala:
        break
    for i in range (escala):
        for j in range (escala):
            if i == h and j == v:
                print('X', end=" ")
            else:
                print('O', end=" ")
        print ('\n')

    move = input ('Faça seu primeiro movimento sem sair do tabuleiro e usando apenas WASD: ')
    if move.lower() not in functions:
        print ('Faça um movimento válido vacilão')
    if move.lower() == 'w':
        h=h-1
    if move.lower() == 'a':
        v=v-1
    if move.lower() == 's':
        h=h+1
    if move.lower() == 'd':
        v=v+1

print(fim)