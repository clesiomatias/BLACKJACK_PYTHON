#-*-coding: utf-8 -*-

'''Clone do jogo clássico 21
    Programado de forma procedural
    Linguagem Python
    Módulos Turtle e Pygame'''

__author__ = 'Clésio Matias <clesiofmatias@gmail.com>'
__version__ = '1.0'


#---------IMPORTS NECESSÁRIOS---------------#
import turtle
import pygame
import random
from time import sleep
pygame.init()# iniciando pygame
    #fim de imports
#--------
    #escopo global
face = ('a','2','3','4','5','6','7','8','9','10','j','q','k')
naipe = ('c','o','e','p')
tipo = '.gif'
deck = {}
deckimg=[]#lista que guarda os nomes de todas as imagens
deckv = [1,2,3,4,5,6,7,8,9,10,10,10,10,
         1,2,3,4,5,6,7,8,9,10,10,10,10,
         1,2,3,4,5,6,7,8,9,10,10,10,10,
         1,2,3,4,5,6,7,8,9,10,10,10,10]#lista dos valores das cartas
decknomes = []#lista dos nomes das cartas
valor = {} #dicionario das cartas montadas com valor
posição = -50 #posição no eixo 'x' que as cartas ocupam no campo
credito = 100 #saldo para apostas que o jogador tem,iniciando com $100
score = 0 # quantidade de pontos que o jogador tem
aposta =0 # variavel de controle de apostas
as_onze =0 # variavel que controla se um ás é comprado junto com uma carta valor 10
jogando = True # variavel de controle do loop de jogo
recomeço = True #variavel de continuação do jogo
label_score = turtle.Turtle()#rotulo de score
hud = turtle.Turtle()
janela = turtle.Screen()

    #registrando imagem de fundo e imagens de escolha sim e nao
turtle.register_shape('fundo.gif')
turtle.register_shape('nao.gif')
turtle.register_shape('sim.gif')

     #Registrando os sons do jogo
musica = pygame.mixer.Sound('musica.wav')
cartear = pygame.mixer.Sound('cartear.wav')
baralho = pygame.mixer.Sound('baralho.wav')
moedas = pygame.mixer.Sound('moedas.wav')
palmas = pygame.mixer.Sound('palmas.wav')
derrota = pygame.mixer.Sound('derrota.wav')


    #fim do escopo global

#---------------CRIANDO A JANELA-----------#
def cria_janela():
    global jogando
    jogando=True
    turtle.setup(800,600)
    turtle.ht()    
    janela.bgcolor('black')
    janela.title('BlackJack')

    #---------------CRIANDO A BANCA DE JOGO-------#
        #inicio criação aro verde
    aro = turtle.Turtle()
    aro.setposition(-390,300)
    aro.pensize(10)
    aro.setheading(270)
    aro.color('green')
    aro.fillcolor('green')
    aro.speed(0)
    aro.begin_fill()
    aro.circle(385,180)
    aro.setpos(-390,300)
    aro.end_fill()
    aro.penup()
        #fim criação aro verde
    #---------
        #inicio criação aro amarelo
    aro_amarelo = turtle.Turtle()
    aro_amarelo.ht()
    aro_amarelo.pensize(25)
    aro_amarelo.setheading(300)
    aro_amarelo.speed(0)
    aro_amarelo.penup()
    aro_amarelo.setpos(-265,240)
    aro_amarelo.pendown()
    aro_amarelo.color('yellow')
    aro_amarelo.circle(300,117)
    aro_amarelo.penup()
        #fim da criação do aro amarelo
    #--------
        #inicio da criação dos quadros de compra e stando do baralho
    stand1 = turtle.Turtle()
    stand1.ht()
    stand1.penup()
    stand1.setpos(-50,-50)
    stand1.pensize(5)
    stand1.speed(0)
    stand1.color('yellow')
    stand1.pendown()
    stand1.fd(60)
    stand1.lt(90)
    stand1.fd(110)
    stand1.lt(90)
    stand1.fd(60)
    stand1.lt(90)
    stand1.fd(110)
    stand1.lt(90)

    stand2 = turtle.Turtle()
    stand2.ht()
    stand2.penup()
    stand2.setpos(-50,150)
    stand2.pensize(5)
    stand2.speed(0)
    stand2.color('blue')
    stand2.pendown()
    stand2.fd(60)
    stand2.lt(90)
    stand2.fd(110)
    stand2.lt(90)
    stand2.fd(60)
    stand2.lt(90)
    stand2.fd(110)
    stand2.lt(90)
        #fim da criação dos quadros de compra e stando do baralho
    #---------
        #criação da HUD e score de jogo
    
    hud.penup()
    hud.ht()
    hud.color('white')
    hud.setpos(-380, 270)
    hud.write(f'Seu crédito é : ${credito}',False, font=('Arial Rounded',14,'bold'))

    
    label_score.penup()
    label_score.ht()
    label_score.color('white')
    label_score.setpos(-80,-270)
        #fim da criação de HUD e score
    #-------
        #criando o baralho que ficará visivel somente o fundo, e sera de onde será compradas todas as cartas
    pygame.mixer.Sound.play(baralho)    #tocando som de baralho
    baralho_da_mesa = turtle.Turtle()
    baralho_da_mesa.penup()
    baralho_da_mesa.setpos(-20,200)
    baralho_da_mesa.speed(0)
    baralho_da_mesa.st()
    baralho_da_mesa.shape('fundo.gif')
        #fim da criação do baralho da banca
        
#------- CRIANDO AS CARTAS---------#
def deck_build():
    global naipe, face,deckimg, decknomes,valor
    
        #Registrando imagens:
    for n in naipe:
        for f in face:
            deckimg.append(f'{f+n+tipo}')
    #print(deckimg,f'\ntotal de itens {len(deckimg)}')#---------------------------------teste
    for i in deckimg:
        #print(f'{i}')#-----------------------------------------------------------------teste
        turtle.register_shape(i)
        #fim do registro de imagens
    #---------
        #Registrando os nomes
    for i in naipe:
        for c in face:
           decknomes.append(f'{c+i}')
    #print(decknomes,f'\ntotal de itens {len(decknomes)}')#------------------------------teste
        #fim do registro de nomes
    #---------
        #Anexando valor as cartas em um dicionario
    valor=dict(zip(decknomes,deckv))
    #print(valor,f'\ntotal de itens {len(valor)}')#------------------------------teste
    
        #fim do registro de valores
#----------
        #criação da função main
    
def main():
    global credito,score,janela, jogando, posição
    
    posição = -50 #resetando a pocição inicial das cartas
    jogando = True # retornando a função jogando
    janela.clear()#limpando janela pra re-criar
    cria_janela() #rodando a musica de fundo
    pygame.mixer.Sound.play(musica)#"soltando" a música de fundo
    musica.set_volume(0.3)#regulando volume da música de fundo
    #montando o baralho
    deck_build()
    #re-escrevendo o saldo
    hud.clear()
    hud.write(f'Seu crédito é : ${credito}',False, font=('Arial Rounded',14,'bold'))
    
    #verificando saldo de creditos:
    if credito<=0:
        gameover()
      
    else:
        #recebendo aposta
        aposta = int(janela.numinput("Sua Aposta", "Quanto quer apostar?:", 10, minval=1, maxval=credito))
        credito-=aposta
        hud.clear()
        hud.write(f'Seu crédito é : ${credito}',False, font=('Arial Rounded',14,'bold'))
            
        #comprando as primeiras duas cartas
        comprar(2)

        #se vierem de cara um ás e uma carta valor dez
        if score ==11 and as_onze==11:
               score=21
               label_score.clear()
               label_score.write(f'Você tem {score} pontos', False, font=('Arial Rounded',14,'bold'))
        #loop de analise do jogo. até ganhar, perder ou desistir
        while jogando:
            analise()
               
        #fim da criação da função main
#---------
        #criação das funções recomeçar e over
               
def recomeçar(x,y):
    global score
    score=0
    main()
    
def over(x,y):
    global janela
    janela.clear()
    mensagem = turtle.Turtle()
    mensagem.penup()
    mensagem.ht()
    mensagem.color('red')
    mensagem.setpos(0,0)
    mensagem.write(f'OBRIGADO POR JOGAR!\nSEU CRÉDITO FINAL FOI DE ${credito}', False, font=('Aral Rounded',28,'bold'), align = 'center')
    sleep(2)
    janela.bye()

        #fima da criação das funções recomeçar e over

#---------
        #criação da função comprar
    
def comprar(n):
    global decknomes,valor,tipo,posição,score,cartear, as_onze
    for i in range(0,n):
        e = random.choice(decknomes)
        decknomes.remove(e)
        score += valor[e]
        if valor[e]==1: 
            as_onze =11
        carta = turtle.Turtle()
        carta.ht()
        carta.penup()
        carta.shape(e+tipo)
        carta.setpos(posição,0)
        posição+=25
        carta.st()
        pygame.mixer.Sound.play(cartear)
        #atualizando o score
        label_score.clear()
        label_score.write(f'Você tem {score} pontos', False, font=('Arial Rounded',14,'bold'))

        # fim da criação da função comprar
#-------------
        #criação da função janela parabéns
    
def parabens():
    #a função credita o valor da aposta + 50%
    #nos creditos e emite uma mensagem de parabéns
    global credito,musica,palmas,moedas
    pygame.mixer.Sound.stop(musica)
    pygame.mixer.Sound.play(moedas)
    pygame.mixer.Sound.play(palmas)
    credito+=aposta+aposta/2
    janela.clear()
    parabens = turtle.Turtle()
    parabens.penup()
    parabens.ht()
    parabens.color('red')
    parabens.setpos(0,0)
    parabens.write('VOCÊ VENCEU!PARABÉNS!', False, font=('Aral Rounded',36,'bold'), align = 'center')
    
    sleep(5)
    
        #fim da criação da função janela parabéns
#-----------
        #criação da janela de escolha

def escolha():
    global janela,score
    score=0
    janela.clear()
    pygame.mixer.Sound.stop(musica)
    mensagem = turtle.Turtle()
    mensagem.penup()
    mensagem.ht()
    mensagem.setpos(0,0)
    mensagem.write('JOGAR NOVAMENTE?', False, font=('Aral Rounded',36,'bold'), align = 'center')
    sim  = turtle.Turtle()
    sim.penup()
    sim.color('yellow')
    sim.setpos(-150,-100)                
    sim.shape('sim.gif')
    sim.onclick(recomeçar)

    nao = turtle.Turtle()
    nao.penup()
    nao.color('yellow')
    nao.setpos(150,-100)
    nao.shape('nao.gif')
    nao.onclick(over)

        #fim da criação da janela escolha
#-----------
        #criação da janela perdeu
def perdeu():
    global janela, derrota, musica
    pygame.mixer.Sound.stop(musica)
    pygame.mixer.Sound.play(derrota)
    
    janela.clear()
    perdeu = turtle.Turtle()
    perdeu.penup()
    perdeu.ht()
    perdeu.color('red')
    perdeu.setpos(0,0)
    perdeu.write('INFELIZMENTE VOCÊ PERDEU!', False, font=('Aral Rounded',36,'bold'), align = 'center')
    sleep(4)
    
#-----------
        #criação da janela game over

def gameover():
    global janela
    janela.clear()
    pygame.mixer.Sound.stop(musica)
    gameOver = turtle.Turtle()
    gameOver.penup()
    gameOver.ht()
    gameOver.color('red')
    gameOver.setpos(0,0)
    gameOver.write('GAME OVER\n SALDO INSUFICIENTE!', False, font=('Aral Rounded',36,'bold'), align = 'center')
    # fim da criação da janela game over
#-----------

    #criação da função de analise do jogo
def analise():
    global janela, score, jogando
    global credito ,recomeço
    if score ==21:
        jogando = False
        parabens()
        escolha()
    elif score >21:
        if credito >0:
            jogando = False
            perdeu()
            escolha()
        else:
            jogando = False 
            gameover()
    else:
        while score < 21 and recomeço:
            decida = janela.textinput('Comprar novamente?','S/N')
            if decida in 'Ss':
                mais_cartas = int(janela.numinput(f"Você tem {score} pontos", "Quantas cartas quer?", 1, minval=1, maxval=len(decknomes)))
                comprar(mais_cartas)
            elif decida in 'Nn':
                recomeço =False
                escolha()
    #fim da criação da função de analise do jogo

                
#-----------  CHAMADA DO LOOP DO JOGO ----------#

main()    
                    

