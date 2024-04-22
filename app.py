from random import randint #Importando a biblioteca random
from time import sleep #Importando a biblioteca  time
from colorama import Fore  #Inportando abiblioteca colorama



def inicio(): #Função que da inicio ao jogo
    return inicio
while True : #Loop que mantem o  jogo depois de verificar se o nick e maior que 3 caracteres  nick
 print( Fore.WHITE+ '-'*70)
 print('Òla eu sou o computador seu adversario,qual seu nick?')
 print('-'*70)
 name = input('->  ') #Usuario insere o nick 
 tamnho = len(name) #Variavel quer ler a quantidade dos caracteres

 if tamnho >= 3: #Função que verificar se o nick possui mais de 3 caracteres
  print( f'Seja bem vindo(a) {Fore.GREEN} {name}')
  break
 else:
  print(Fore.RED + 'Digite um nick valido') #Caso não tenha esta mensagem ira aparecer e pedira para que digite um novo




def jogo(jokenpo): #Função que inicia o jogo 
 return jogo
rodadas = 0 #Antes que a primeira jogada seja feita as rodadas seram 0
jogando = True
while jogando:#Loop que mantem e o jogo depois de escolher as opções
 itens = ['pedra', 'tesoura', 'papel'] #Variavel que armazenas o valores jogaveis
 computador = randint(0,2) #Função randint que escolhe de forma aletoria os valores das jogadas do computador
 print('-'*28)
 print(Fore.LIGHTBLUE_EX + 'Vamos nessa!!!')
 sleep(1.2) #Tempo de atraso
 print( Fore.BLUE + '''
      Faça sua escolha
      [0] PEDRA
      [1] TESOURA 
      [2] PAPEL
      ''')
 while True:
        player = input(Fore.WHITE+ '-> ') # O usuário insere sua escolha

        if player in ['0', '1', '2']: # Verifica se a escolha do jogador é válida
            player = int(player)
            break
        else:
            print(Fore.RED + 'Opção inválida! Por favor, escolha entre 0, 1 ou 2.')
 

 print(Fore.GREEN + 'JO')
 sleep(1)#Tempo de atraso
 print(Fore.YELLOW+'kEN')
 sleep(1)#Tempo de atraso
 print(Fore.MAGENTA+'PO!!!')
 print(Fore.WHITE+'-=-='*11)
 print('O jogador jogou {}'.format(itens[player])) #Print com o valor que o usario jogou
 print('O computador jogou {}'.format(itens[computador]))#Print com o valor que o computador escolheu 
 print('-=-='*11)

#Funçao que verifica e determina o valor de acordo com as regras do jodo ex: pedra > tesoura
 if player == computador: #Se o computador escolher igual ao usuario o jogo empata
       print( Fore.YELLOW +  'EMPATE!!!')
 
 elif player == 1:
  if computador != 0:
      ganhador =  print(Fore.GREEN + 'Você venceu') #Se o usurio for tesoura(1) e o computador for diferente de pedra(0) o usuario vence
  else:
       print( Fore.RED + 'O computador ganhou')#Se for ao contrario e computador vence
 elif player == 0:#Se o usurio for pedra(0) e o computador for diferente de papel(2) o usuario vence
  if computador != 2:
       print(Fore.GREEN + 'Você venceu')
   
  else:
      print( Fore.RED + 'O computador ganhou')#Se for ao contrario e computador vence
 elif player == 2:
  if computador != 1:
      ganhador = print(Fore.GREEN + 'Você venceu')

   #Opção que pede ao usuario que informe se deseja continuar ou não
 def conituarPara(opcoe):
      return conituarPara
 while True:
      print(Fore.LIGHTBLUE_EX + 'Deseja continuar? S/N')
      opcao = input('-> ').upper() #Input que armazena os valores digitados pelo usuario
      if opcao == 'N': #Se a escolha for não(N) o jogo sera parado e o numero de jogadas feitas é exibido
       print(Fore.LIGHTGREEN_EX + 'Jogo encerrado,TCHAU!!! ')
       print( f'Rodadas jogadas {rodadas  + 1}')
       jogando = False
       sleep(7)
       break
      
       

      if opcao == 'S':#Se a escolha for sim(s) o jogo continuara ate ser encerrado numero de jogadas feitas é exibido
       print( f'Rodada {rodadas  + 1}')
       rodadas += 1
       jogo
       break
      
      else:
       print(Fore.RED + 'ERROR!!!Digite uma opção valida')
       conituarPara

