#-*-coding: utf-8 -*-

##Clone do jogo clássico 21
##Programado de forma procedural
##Linguagem Python 3.6

__author__ = 'Clésio Matias <clesiofmatias@gmail.com>'
__version__ = '1.0'

#---------IMPORTS NECESSÁRIOS---------------#
import random
import time

#----------ESCOPO GLOBAL -------------------#
credito =100 
valores =0#variavel de controle de vitória e derrota
valor={}#dicionario que anexa valor às cartas
jogando = True #variavel de controle do loop do jogo
as_onze=0 #variavel que controla se um ás é comprado junto com uma carta valor 10

#variaveis de montagem das cartas
face = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
naipe = ( "♥","♣", "♦", "♠")

#lista dos valores das cartas
deckv = [1,2,3,4,5,6,7,8,9,10,10,10,10,
         1,2,3,4,5,6,7,8,9,10,10,10,10,
         1,2,3,4,5,6,7,8,9,10,10,10,10,
         1,2,3,4,5,6,7,8,9,10,10,10,10]

deck =[] #lista das cartas montadas

#-----------------FUNÇÕES DO JOGO-----------------#

#função de criar baralho
def deckBuild():
    global naipe
    global face
    global deck
    global decv
    global valor
    #--------------CRIANDO O DECK -------------#
    
    for n in naipe:
        for f in face:
            carta = f+n
            deck.append(carta)
            
            

    #-------------- ANEXANDO VALORES ÀS CARTAS--------#
    valor=dict(zip(deck,deckv))
    '''A função built-in zip do Python retorna uma lista
    contendo tuplas, onde o primeiro valor é o da primeira lista,
    e o segundo valor da tupla, corresponde a segunda lista'''



#função de embaralhar
def embaralhar():
    random.shuffle(deck)
    
#função comprar
def comprar(n):
    global valores
    global as_onze
    '''Esta função recebe um inteiro com a quantidade
       de cartas a serem compradas, na sequencia elimina
       as mesmas do baralho'''
    for i in range(0,n):
        e = random.choice(deck)
        deck.remove(e)
        print(e,end='-')
        valores+= valor[e]
        if valor[e]==1: 
            as_onze =11
    
    print('')
    
#----------- LOOP DO JOGO ----------#

while jogando:
    # criando e embaralhando as cartas:
    deck=[]
    deckBuild()
    embaralhar()
    
    #verficando saldo de creditos
    if credito<=0:
        print('Saldo insuficiente para continuar jogando, desculpe!')
        break
    
    recomeço=False #variavel que controla se é o começo do jogo
    
    #----criando o cabeçalho
    print('-='*35)
    print('CLÁSSIC GAME BLACKJACK')
    print('-='*35)
    print(f'Seu saldo é de ${credito}')
    #-----fim cabeçalho

    #-----recebendo e validando aposta
    while True:
        aposta = input('Digite o valor da aposta: ')
        if aposta.isnumeric()and float(aposta)<= credito:
            aposta = float(aposta)
            credito-=aposta #reduzindo valor da aposta nos creditos
            
            break
        else:
            print('Aposta inválida. Digite o valor de sua aposta')
    #------aposta validada

    #----pontinhos com pausa dramática :)
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.', end='')
    print('.')
    #-------fim dos pontinhos

    comprar(2) # primeiras duas cartas
    

    #se vierem de cara um ás e uma carta valor dez
    if valores ==11 and as_onze==11:
        valores=21

    #resolvendo se ganhou, perdeu ou se quer mais cartas:
    while recomeço == False:
            #ganhando!
            if valores == 21:
                credito+=aposta+aposta/2
                print(f'PARABÉNS VOCÊ GANHOU!!!\n Seu novo saldo de créditos é: ${credito}')

                #reiniciando ou não
                novo_jogo = input('Jogar novamente? [S/N]')
                while True:
                    if novo_jogo in 'Ss':
                         valores=0
                         recomeço = True
                         break
                    elif novo_jogo in 'Nn':
                          print('Até a próxima!')  
                          jogando =False
                          recomeço=True
                          break
                    else:
                        print('Opção inválida!')
                        novo_jogo = input('Jogar novamente? [S/N]')


                    #com menos de 21
            elif valores<21:
                
                #continuando ou desistindo
                while valores < 21:
                    print(f'Você tem {valores} pontos.')
                    continuar = input('Deseja mais cartas? [s/n]')
                    
                    if continuar in 'Ss':
                        # validando entrada e comprando novas cartas
                        while True:
                            cartas = input('Quantas cartas quer? ')
                            if cartas.isnumeric():
                                cartas=int(cartas)
                                comprar(cartas)
                                break                             
                            else:
                                print('Quantidade Inválida!')
                                continue
                        break
                    
                    elif continuar in 'Nn':
                        novo_jogo = input('Jogar novamente? [S/N]')
                        while True:
                            if novo_jogo in 'Ss':
                                 valores=0
                                 recomeço = True
                                 break
                            elif novo_jogo in 'Nn':
                                  print('Ate a próxima!')
                                  jogando =False
                                  recomeço = True
                                  break
                            else:
                                print('Opção inválida!')
                                novo_jogo = input('Jogar novamente? [S/N]')
                                break
                            
                    break

                
                    #perdendo
            else:
                print(f'Voce perdeu! Estourou com {valores} pontos')
                print(f'Seu saldo de creditos é de ${credito}')
                novo_jogo = input('Jogar novamente? [S/N]')
                while True:
                    if novo_jogo in 'Ss':
                         valores=0
                         recomeço = True
                         break
                    elif novo_jogo in 'Nn':
                          jogando =False
                          recomeço = True
                          break
                    else:
                        print('Opção inválida!')
                        novo_jogo = input('Jogar novamente? [S/N]')
            
                        
                
    
    




