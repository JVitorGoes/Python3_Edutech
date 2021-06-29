import random

def jogar():
  
  def frase_com_detalhe(frase):
    print("=================================")
    print(frase)
    print("=================================")
    #33 letras

  def random_aleatorio():
    numero_random = random.randrange(1, 101)
    return numero_random

  frase_com_detalhe("Bem Vindo ao jogo de Adivinhação!")

  numero_secreto = random_aleatorio()
  total_de_tentativas = 0
  pontos = 1000

  print("Qual o seu nível de dificuldade?")
  print("[1] Fácil [2] Médio [3] Difícil")

  nivel = int(input("Defina o nível: "))
  if nivel == 1:
    total_de_tentativas = 20
  elif nivel == 2:
    total_de_tentativas = 10
  elif nivel == 3:
    total_de_tentativas = 5
  else:
    print("Nível não disponível!")

  for rodada in range(1, total_de_tentativas + 1):

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
      print("Você DEVE digitar um número entre 1 e 100!")
      continue

    acertou = (numero_secreto == chute)
    acima = (numero_secreto < chute)
    abaixo = (numero_secreto > chute)

    if (acertou):
      print("Você acertou em {} tentativas e fez {} pontos!".format(rodada, pontos))
      break
    else:
      if (acima):
        print("Você errou! Seu chute foi acima do esperado.")
      elif (abaixo):
        print("Você errou! Seu chute foi abaixo do esperado.")
      pontos_perdidos = abs(numero_secreto - chute)
      pontos = pontos - pontos_perdidos

  frase_com_detalhe("======== FIM DE JOGO!!! =========")

if (__name__ == "__main__"):
  jogar()