import random

def frase_com_detalhe(frase):
    print("=================================")
    print(frase)
    print("=================================")
    #33 letras

#Início
def jogar():

  frase_com_detalhe("== Bem Vindo ao jogo da Forca! ==") 
  palavra_secreta = carrega_palavra_secreta()
  letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

  enforcou = False
  acertou = False
  erros = 0

  print(letras_acertadas)

  while (not enforcou and not acertou):

    tentativas = 7 - erros
    print("Tentativas: {}".format(tentativas))

    chute = pede_chute()

    if (chute in palavra_secreta):
      marca_chute_correto(palavra_secreta, chute, letras_acertadas)
    else:
        erros += 1
        desenha_forca(erros)

    enforcou = erros == 7
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)

  if(acertou):
    imprime_mensagem_vencedor()
  else:
    imprime_mensagem_perdedor(palavra_secreta)

  frase_com_detalhe("======== FIM DE JOGO!!! =========")
#Fim

def carrega_palavra_secreta():
  arquivo = open("frutas.txt", "r")
  palavra = []
  for linha in arquivo:
    linha = linha.strip()
    palavra.append(linha)
  arquivo.close()
  numero = random.randrange(0, len(palavra))
  palavra_secreta = palavra[numero].upper()
  return palavra_secreta

def inicializa_letras_acertadas(palavra):
  return ["_" for letras in palavra]

def pede_chute():
  chute = input("Escreva uma letra: ")
  chute = chute.strip().upper()
  return chute

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
  index = 0
  for letra in palavra_secreta:
    if (chute == letra):
      letras_acertadas[index] = letra
    index += 1 

def imprime_mensagem_perdedor(palavra_secreta):
  print("Você foi Enforcado!!!")
  print("A palavra era {}!".format(palavra_secreta))
  print("    _______________         ")
  print("   /               \       ")
  print("  /                 \      ")
  print("//                   \/\  ")
  print("\|   XXXX     XXXX   | /   ")
  print(" |   XXXX     XXXX   |/     ")
  print(" |   XXX       XXX   |      ")
  print(" |                   |      ")
  print(" \__      XXX      __/     ")
  print("   |\     XXX     /|       ")
  print("   | |           | |        ")
  print("   | I I I I I I I |        ")
  print("   |  I I I I I I  |        ")
  print("   \_             _/       ")
  print("     \_         _/         ")
  print("       \_______/           ")

def imprime_mensagem_vencedor():
  print("Parabéns, você acertou!")
  print("       ___________      ")
  print("      '._==_==_=_.'     ")
  print("      .-\\:      /-.    ")
  print("     | (|:.     |) |    ")
  print("      '-|:.     |-'     ")
  print("        \\::.    /      ")
  print("         '::. .'        ")
  print("           ) (          ")
  print("         _.' '._        ")
  print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
  jogar()