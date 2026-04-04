#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

"""
Exercício: Reprodutor de MP3 com play e pause
Biblioteca utilizada: pygame
Instalação: pip install pygame
"""

import pygame
import time

# Inicializa o mixer do pygame (responsável pelo áudio)
pygame.mixer.init()

# -----------------------------------------------
# Coloque aqui o caminho do seu arquivo MP3
arquivo_mp3 = "YE - KING.mp3"
# -----------------------------------------------

# Carrega o arquivo MP3
pygame.mixer.music.load(arquivo_mp3)

print("=== Reprodutor de MP3 ===")
print("Comandos: [p] play | [s] pause | [q] sair")
print()

pausado = False

while True:
    comando = input("Digite o comando: ").strip().lower()

    if comando == "p":
        if pausado:
            pygame.mixer.music.unpause()  # Continua de onde parou
            pausado = False
            print("▶ Continuando...")
        else:
            pygame.mixer.music.play()     # Começa do início
            print("▶ Tocando...")

    elif comando == "s":
        pygame.mixer.music.pause()        # Pausa sem perder o progresso
        pausado = True
        print("⏸ Pausado.")

    elif comando == "q":
        pygame.mixer.music.stop()
        print("⏹ Encerrando o player. Até mais!")
        break

    else:
        print("Comando inválido! Use: p (play), s (pause), q (sair)")