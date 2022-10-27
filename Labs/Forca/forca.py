# Jogo da Forca 
# Programação Orientada a Objetos

# Import
import random
from turtle import rt

# tabuleiro (lista)
tabuleiro = ['''

>>>>>>>>>>Forca<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class forca :

     #metodo construtor
     def __init__(self,palavra):
          self.palavra = palavra
          self.erros = []
          self.acertos = []
    
     #metodo para saber se a letra esta correta
     def adivinha(self,letra):
          if letra in self.palavra and letra not in self.acertos:
               self.acertos.append(letra)
          elif letra not in self.palavra and letra not in self.erros:
               self.erros.append(letra)
          else:
               return False
          return True
     
     #verifica se ganhou o jogo
     def ganhou(self):
          if '_' not in self.pEscondida():
               return True
          return False
         
     #verifica se perdeu o jogo
     def acabou(self):
          return self.ganhou() or (len(self.erros) == 6)
     
     #metodo para esconder a palavra
     def pEscondida(self):
          x = ''
          for letra in self.palavra:
               if letra not in self.acertos:
                    x += '_'
               else:
                    x += letra
                  
          return x
     
     #mostrando o visual do jogo
     def print_jogo(self):
          print(tabuleiro[len(self.erros)])
          print ('\n Palavra: '+ self.pEscondida())
          print ('\n Letras erradas:')
          for letra in self.erros:
               print(letra)
          print()
          print("letras corretas:")
          for letra in self.acertos:
               print(letra)
          print()
#definindo a palavra do banco de palavras
def rand_palavra():
     with open("palavras.txt","rt") as f:
          banco = f.readlines()
     return banco[random.randint(0,len(banco))].strip()

def main():
     jogo = forca(rand_palavra())

     while not jogo.acabou():
          jogo.print_jogo()
          letra_usuario = input('\ndigite uma letra: ')
          jogo.adivinha(letra_usuario)

     jogo.print_jogo()

     if jogo.ganhou():
          print('\n Parabéns! voce ganhou o jogo')
     else:
          print('\n Game Over! xp')
          print('\n A palavra era: '+jogo.palavra)

# Executa o programa		
if __name__ == "__main__":
	main()

