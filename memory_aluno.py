import pygame, sys
import random
from pygame.locals import *

'''
ATENCAO: procure pelas marcações 'TODO', pois elas indicam 
onde deverá ser codificado. Leia os comentarios ao longo do 
código. Leia a documentação do pygame para os métodos que você
tiver dúvida.
'''

# Constantes
FPS = 60
W_SIZE = [800, 100]
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 139, 34)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CLOCK = pygame.time.Clock()

NUMBER_CARDS = 16
CARD_SIZE = [W_SIZE[0]/NUMBER_CARDS, W_SIZE[1]]

# setup inicial da biblioteca e da janela - DISPLAYSURF é onde desenham-se os elementos
pygame.init()
DISPLAYSURF = pygame.display.set_mode((W_SIZE[0], W_SIZE[1]))
pygame.display.set_caption('Memory')
pygame.time.set_timer(pygame.USEREVENT, 1000) # veja na doc. do pygame

# Helpers
def init():
   """ Inicializa variaveis globais """
   global deck_cards, exposed, cards_clicked, cards_paired
   global state, number_turns, t_count, font_surf, font_messg, surf_messg

   define_message("")
   t_count = 0 # conta os segundos
   state = 0 # estado do jogo: relativo as cartas viradas pelo usuario (uma ou duas)
   number_turns = 0 # numero de turnos (duas cartas viradas = 1 turno)
   cards_clicked = [] # salva o par de cartas clicadas, pelos seus indices
   cards_paired = 0 # quantidade de pares de cartas descobertas
   # cartas do jogo
   deck_cards = [(str(i) if i < NUMBER_CARDS/2 else str(NUMBER_CARDS%i)) for i in range(NUMBER_CARDS)]
   random.shuffle(deck_cards)
   exposed = [False] * NUMBER_CARDS # guarda os indices relativos ao deck de cartas

   # texto para as cartas: repare que ele é relativo ao deck de cartas
   font_obj = pygame.font.Font('freesansbold.ttf', 50)
   font_surf = []
   for c in deck_cards:
      surf = pygame.font.Font.render(font_obj, c, True, WHITE)
      rect = surf.get_rect()
      font_surf.append([surf, rect])

   # texto para a mensagem no fim do jogo
   font_messg = pygame.font.Font('freesansbold.ttf', 20)
   surf_messg = pygame.font.Font.render(font_messg, msg_intro, True, YELLOW)


def define_message(msg):
   """ Mostra menssagens """
   global msg_intro
   msg_intro = msg
   

# Event handlers
def timer_handler():
   """ Contador do tempo (seg.):
   O comando pygame.time.set_timer(pygame.USEREVENT, 1000) customiza
   um evento (USEREVENT) que sera disparado a cada segundo. Esse evento 
   sera capturado (no loop principal) e esta funcao sera chamada.
   """
   global t_count
   t_count += 1
    

def draw():
   """ Desenha """
   global font_surf

   i = 0
   j = CARD_SIZE[0] / 2
   for x in range(NUMBER_CARDS):
      ''' 
      TODO: Se uma carta estiver exposta, entao o vetor 'font_surf' 
      deve ser usado para centralizar a sua posicao. Caso contrario,
      um poligono deve ser desenhado. A variável 'j' irá auxiliar para
      definir posicao central do texto da carta, enquanto a variavel 'i' 
      irá te auxiliar a definir a posicao do poligono. Pense em como
      você também pode usar a variavel 'CARD_SIZE' para definir os pontos
      do polígono.
      '''
      if exposed[x]:
         # aqui vc deve completar com codigo
      else:
         # aqui vc deve completar com codigo


      i += CARD_SIZE[0]
      j += CARD_SIZE[0]
   pass


def mouse_click(pos):
   """ 
   Recupera o indice da carta clicada e
   atualiza o numero de turnos 
   """
   global state, number_turns, cards_clicked, cards_paired
   global msg_intro, exposed, surf_messg
   
   # indice da carta
   # TODO: recuperar o indice da carta clicada pelo local do clique
   index = # aqui vc deve completar com codigo
   if not exposed[index]:
      if state == 0:
         state = 1
      elif state == 1:
         state = 2
         number_turns += 1 # fim de um turno

         # TODO: determinar o fim do jogo
         if : # aqui vc deve completar com codigo
            define_message("Otimo! Voce terminou em " + str(t_count//60) + "min" + str(t_count%60) + "segs.")
            surf_messg = pygame.font.Font.render(font_messg, msg_intro, True, YELLOW)
      else:
         state = 1
         '''
         TODO: aqui deve existir um teste condicional para esconder a dupla de cartas
         que o usuario tentou advinhar, mas não eram iguais. Essas cartas devem ser
         escondidas novamente.
         '''
         if : # aqui vc deve completar com codigo
            # aqui vc deve completar com codigo
         else:
            cards_paired += 1

         cards_clicked = []

      cards_clicked.append(index)
      exposed[index] = True
   

def main():
   global font_surf, surf_messg

   init()
   while True:
      DISPLAYSURF.fill(GREEN)

      for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
         if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse_click(pos)
         if event.type == pygame.USEREVENT:
            timer_handler()

      # desenha
      draw()
      for x in range(NUMBER_CARDS):
         if exposed[x]:
            DISPLAYSURF.blit(font_surf[x][0], font_surf[x][1])

      DISPLAYSURF.blit(surf_messg, [5, W_SIZE[1]-20])

      pygame.display.update()
      CLOCK.tick(FPS)

main()