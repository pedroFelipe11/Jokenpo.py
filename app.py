from random import randint #Importando a biblioteca random
from time import sleep #Importando a biblioteca  time
from colorama import Fore  #Importando abiblioteca colorama
import sqlite3 #importando o sqlite3

conectionJk = sqlite3.connect("Jokenpô.db") # Estabelece uma conexão com o banco de dados SQLite denominado "Jokenpô.db"
cursorJk = conectionJk.cursor()  #Cria um objeto cursor para interagir com o banco de dados SQLite usando a conexão estabelecida


def create_table():
        # Criar tabela no banco de dados se ainda não existir
         cursorJk.execute('''CREATE TABLE IF NOT EXISTS Jokenpo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nomeJg TEXT,
                    rodadasJogadas INT,
                    rodadasGanhas INT,
                    rodadasEmpatadas INT,
                    rodadasPerdidas INT          
                )''') 
         
create_table()
    # Executa uma consulta SQL para selecionar todos os dados do jogador com o nome especificado na tabela Jokenpo
def dataentry(nameJg, round , roundsWon , tiedRounds, lostRouns ):
    cursorJk.execute("SELECT * FROM Jokenpo WHERE nomeJg=?", (nameJg,))
    # Obtém os dados do jogador, se existirem    
    player_data = cursorJk.fetchone() 
    if player_data:
        # Se o jogador já existe, atualize as rodadas jogadas
        new_rodadas = player_data[2] + round # Soma o número de rodadas jogadas com as novas rodadas
        new_rodadasWon = player_data[3] + roundsWon  # Soma o número de rodadas ganhas com as novas rodadas ganhas
        new_tiedRounds = player_data[4] + tiedRounds # Soma o número de rodadas empatadas com as novas rodadas empatadas
        new_lostRouns = player_data[5] + lostRouns   # Soma o número de rodadas perdidas com as novas rodadas perdidas

        cursorJk.execute("UPDATE Jokenpo SET rodadasJogadas = ? , rodadasGanhas = ? , rodadasEmpatadas = ? , rodadasPerdidas = ? WHERE nomeJg=?", (new_rodadas, new_rodadasWon, new_tiedRounds, new_lostRouns, nameJg))
    else:
        # Se o jogador não existe, insira um novo registro
        #Inserindo os dados coletados nas colunas da tabela
        cursorJk.execute("INSERT INTO Jokenpo (nomeJg, rodadasJogadas , rodadasGanhas , rodadasEmpatadas , rodadasPerdidas  ) VALUES( ? , ? , ? , ? , ?)", (nameJg, round , roundsWon , tiedRounds , lostRouns ))
        conectionJk.commit() # Confirma todas as alterações feitas no banco de dados desde o último commit


def updateTable(nameJg, round , roundsWon , tiedRounds,lostRouns):
    cursorJk.execute("UPDATE Jokenpo SET rodadasJogadas = ? , rodadasGanhas = ? , rodadasEmpatadas = ? , rodadasPerdidas = ?   WHERE nomeJg=?", (round,  roundsWon , tiedRounds , lostRouns ,nameJg))
    conectionJk.commit() # Confirma todas as alterações feitas no banco de dados desde o último commit


def mostrar_dados(): #funçao que exibe o nome jogadores as rodas jogadas , rodadas ganhadas , perdidas e empatadas por ele
    cursorJk.execute("SELECT * FROM Jokenpo")# Executa a consulta SQL para selecionar todos os dados da tabela Jokenpo
    players = cursorJk.fetchall()# Recupera todos os resultados da consulta e os armazena na lista jogadores

    print(Fore.WHITE + '-'*100)
    print('Informações dos jogadores:')
    print('-'*100)
    # Imprime os rótulos das colunas
    print('{:<10} {:<15} {:<15} {:<15} {:<15} {:<15}'.format('ID', 'Nome', 'Rodadas Jogadas', 'Rodadas ganhas', 'Rodadas empatadas', 'Rodadas perdidas'))
    print('-'*100)
    for jogador in players:
         # Imprime os detalhes de cada jogador formatados nas colunas correspondentes
        print('{:<10} {:<20} {:<15} {:<15} {:<15} {:<15}'.format(jogador[0], jogador[1], jogador[2], jogador[3], jogador[4], jogador[5]))

def top(): #Função que da inicio ao jogo
    return top
while True : #Loop que mantem o  jogo depois de verificar se o nick e maior que 3 caracteres  nick
 print( Fore.WHITE+ '-'*70)
 print('Òla eu sou o computador seu adversario,qual seu nick?')
 print('-'*70)
 nameJg = input('->  ') #Usuario insere o nick 
 sizeName = len(nameJg) #Variavel quer ler a quantidade dos caracteres

 if sizeName >= 3 and sizeName < 15: #Função que verificar se o nick possui mais de 3 caracteres e menor que 20
  print( f'Seja bem vindo(a) {Fore.GREEN} {nameJg}')
  break
 else:
  print(Fore.RED + 'Digite um nick valido') #Caso não tenha esta mensagem ira aparecer e pedira para que digite um novo

def game(jokenpo): #Função que inicia o jogo 
 return game
round = 0 #Antes que a primeira jogada seja feita as rodadas seram 0
roundsWon = 0 # Inicializa a contagem de rodadas ganhas como 0
tiedRounds = 0 # Inicializa a contagem de rodadas empatadas como 0
lostRouns = 0 # Inicializa a contagem de rodadas perdidas como 0
jogando = True # Variável de controle para manter o loop do jogo
while jogando:#Loop que mantem e o jogo depois de escolher as opções
 itens = ['pedra', 'tesoura', 'papel'] #Variavel que armazenas o valores jogaveis
 machine = randint(0,2) #Função randint que escolhe de forma aletoria os valores das jogadas do computador
 print('-'*28)
 print(Fore.LIGHTBLUE_EX + 'Vamos nessa!!!')
 round += 1
 print( f'{round}º rodada')
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
 print('O computador jogou {}'.format(itens[machine]))#Print com o valor que o computador escolheu 
 print('-=-='*11)
  #Verificação de quem ganhou a rodada
 if player == machine: # Se o usuario jogar o mesmo escolhido pelo computador o jogo ser empatado
        print(Fore.YELLOW + 'EMPATE!!!')
        tiedRounds += 1 #toda vez que o jogo terminar empatado sera somado 1 na variavel tiedRounds
           #pedra(0) > tesoura (1)           #tesoura(2) > papel(2)             #papel(2) > pedra(0)
 elif (player == 0 and machine == 1) or (player == 1 and machine == 2) or (player == 2 and machine == 0): #Verificar se o usuario ganhou as rodadas
        print(Fore.GREEN + 'Você venceu')
        roundsWon += 1#toda vez que o o usuario ganhar um round sera somado 1 na variavel roundsWon
 else:
        print(Fore.RED + 'O computador ganhou')#Caso o o usuario nao ganhe sera imprido que o computador ganho e sera adicionado 1 na variavel lostRouns
        lostRouns += 1

 dataentry(nameJg, 1, 1, 1, 1 )# Chama a função dataentry para inserir ou atualizar os dados do jogador no banco de dados
                               #nameJg: Nome do jogador.
                               #1: Indica que o jogador participou de uma rodada.
                               #1: Indica que o jogador ganhou uma rodada.
                               #1: Indica que o jogador empatou uma rodada.
                               #1: Indica que o jogador perdeu uma rodada.
 def decision():
      return decision
 while True:
      print(Fore.LIGHTBLUE_EX + 'Deseja continuar? S/N')
      opcao = input('-> ').upper() #Input que armazena os valores digitados pelo usuario
      if opcao == 'N': #Se a escolha for não(N) o jogo sera parado e o numero de jogadas feitas é exibido
       updateTable(nameJg, round , roundsWon , tiedRounds,lostRouns)# toda vez que o usuario escolher 'n' a tabela sera atualizada
       print(Fore.LIGHTGREEN_EX + 'Jogo encerrado,TCHAU!!! ')
       print( f'Rodadas jogadas {round}') #imprime as rodadas jogadas pelo usuario
       mostrar_dados()
       jogando = False
       sleep(30)
       break
      
       

      if opcao == 'S':#Se a escolha for sim(s) o jogo continuara ate ser encerrado numero de jogadas feitas é exibido
       updateTable(nameJg, round , roundsWon , tiedRounds,lostRouns) #toda vez que o usuario escolher 's' a tabela sera atualizada
       game
       break
      
      else:
       print(Fore.RED + 'ERROR!!!Digite uma opção valida')
       
