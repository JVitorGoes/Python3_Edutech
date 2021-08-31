import adivinhacao
import forca

def frase_com_detalhe(frase):
    print("=================================")
    print(frase)
    print("=================================")
    #33 letras

def escolhe_jogo():

  frase_com_detalhe("== Bem Vindo a Sala de Jogos!!! =")

  jogar_de_novo = True
  i = True

  while jogar_de_novo == True:

    print ("Qual jogo gostaria de jogar? \n(1)Adivinhação (2)Forca (0)Exit")
    jogo = int(input(">>> "))

    if jogo == 1:
      print("Executando Adivinhação...")
      adivinhacao.jogar()
    elif jogo == 2:
      print("Executando Forca...")
      forca.jogar()
    elif jogo == 0:
      print("Exiting...")
      frase_com_detalhe("===== Obrigado por Jogar ;) =====")

    while i == True:

      print ("Deseja jogar novamente? \n(1)Sim (2)Não (0)Outro Jogo")
      resposta = int(input(">>> "))

      if resposta == 0:
        print("Londing...")
        break
      elif resposta == 1:
        if jogo == 1:
          print("Executando Adivinhação...")
          adivinhacao.jogar()
        elif jogo == 2:
          print("Executando Forca...")
          forca.jogar()
      elif resposta == 2:
        i = False
        jogar_de_novo = False
        print("Exiting...")
        frase_com_detalhe("===== Obrigado por Jogar ;) =====")

if (__name__ == "__main__"):
  escolhe_jogo()