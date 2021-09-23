import time

# Biblioteca responsável pela interface
import pygame as p
from pygame.locals import *

# Biblioteca utilizada para gerar números pseudo-aleatórios
import random

# Biblioteca utilizada para matrizes multi-dimensionais
import numpy as np

# Cores em RGB que serão utilizadas na exibição do jogo
BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
RED = (255 , 0 , 0)

# Cria a tela  e determina o tamanho da matriz que será utilizada
root = p.display.set_mode((500 , 400))

# Cria vetor para armazenar as células
cells = np.zeros((root.get_width(),root.get_height()))

# Percorre o vetor e atribui um valor aleatório entre 1 e 100. Caso seja entre 1 e 80 a célula está morta (0), caso esteja entre 80 e 100
# a célula está viva (1)
for i in range(1, root.get_width()-1):
    for j in range(1, root.get_height()-1):
        valor = random.randrange(1,100)
        if 1 <= valor <= 80:
            cells[i][j] = 0
        else: cells[i][j] = 1

# Contador de Gerações
gen = 0

# Loop infinito - O jogo só é encerrado fechando a janela do pygame
while 1:
    print("Geração: ", gen)

    # Encerrar o jogo quando clicar no botão X (Fechar) da janela do pygame
    for i in p.event.get():
        if i.type == QUIT:
            quit()

    # Colorir as células: caso o valor contido na célula seja 0, ela está morta (Cor preta), caso seja 1, ela está viva (cor vermelha).
    for i in range(1 , root.get_width()-1):
        for j in range(0 , root.get_height()-1):
            if cells[i][j] == 0:
                # Usando retângulos de tamanho 20x20x20x20, influencia diretamente na visualização do jogo
                p.draw.rect(root , BLACK , [i * 20 , j * 20 , 20 , 20])
            else: p.draw.rect(root , RED , [i * 20 , j * 20 , 20 , 20])

    # Atualiza o display com as células vivas e mortas
    p.display.update()
    # Pausa para análise da geração
    #time.sleep(5.5)

    # Cria vetor temporário para armazenar a nova geração de células
    cells2 = np.zeros((root.get_width(),root.get_height()))

    # Cria variável temporária para armazenar a quantidade de vizinhos vivos da célula ativa
    count = 0

    # Percorre o vetor para verificar cada célula
    for i in range(1, root.get_width()-1):
        for j in range(1, root.get_height()-1):
            count = 0
            # Vizinho Noroeste
            if cells[i-1][j-1] == 1:
                count +=1
            # Vizinho Norte
            if cells[i-1][j] == 1:
                count +=1
            # Vizinho Nordeste
            if cells[i-1][j+1] == 1:
                count +=1
            # Vizinho Oeste
            if cells[i][j-1] == 1:
                count +=1
            # Caso já tenha mais de 3 vizinhos, morre de superpopulação e posso passar para a próxima célula
            if (count > 3):
                cells2[i][j] = 0 # Superpopulação
                continue
            else:
                # Vizinho leste
                if cells[i][j+1] == 1:
                    count +=1
                # Vizinho sudoeste
                if cells[i+1][j-1] == 1:
                    count +=1
                # Vizinho norte
                if cells[i+1][j] == 1:
                    count +=1
                # Vizinho Sudeste
                if cells[i+1][j+1] == 1:
                    count +=1
                if (count < 2): # Solidão
                    cells2[i][j] = 0
                    continue
                if (count == 3 and cells[i][j] == 0): # Célula morta com 3 vizinhos vivos = célula viva
                    cells2[i][j] = 1
                    continue
                if ((count == 2 or count == 3) and cells[i][j] == 1): # Célula viva com 2 ou 3 vizinhos vivos
                    cells2[i][j] = 1

    cells = cells2
    gen+=1