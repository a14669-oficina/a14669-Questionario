def apresentar_questionario():
  nome = input("\nInsira o seu nome: ")
  print(f"\nBem-vindo {nome}! Responda às seguintes questões:")

  perguntas = [
  "\n1. Como avalia a infraestrutura da escola? (1-5)",
  "2. Como avalia a qualidade dos funcionários? (1-5)",
  "3. Como avalia os equipamentos disponíveis? (1-5)",
  "4. Está satisfeito com a limpeza das instalações? (1-5)",
  "5. Como avalia a experiência dos professores? (1-5)",
  "6. Está satisfeito com as derivadas refeições? (1-5)",
  "7. Recomenda esta escola a outras pessoas? (Sim/Não)",
    ]

  respostas = []

  for pergunta in perguntas:
    resposta = input(pergunta + " ")
    respostas.append(resposta)

  return respostas

def exportar_resultados(respostas):
  nome_ficheiro = input("\nIntroduza o nome do ficheiro para guardar os resultados (ex: resultados.txt): ")
  try:
      with open(nome_ficheiro, "w") as ficheiro:
          ficheiro.write("Respostas ao Questionário de Satisfação\n")
          ficheiro.write("-" * 40 + "\n")
          perguntas = [
          "1. Avaliação da infraestrutura: ",
          "2. Avaliação do atendimento: ",
          "3. Avaliação dos equipamentos: ",
          "4. Satisfação com a limpeza: ",
          "5. Experiência dos professores: ",
          "6. Derivadas refeições: ",
          "7. Recomendação: ",
            ]
          for pergunta, resposta in zip(perguntas, respostas):
              ficheiro.write(pergunta + resposta + "\n")
      print(f"\nResultados guardados com sucesso no ficheiro '{nome_ficheiro}'.")
  except Exception as e:
    print(f"Erro ao guardar o ficheiro: {e}")

def main():
  while True:
      print("-" * 41)
      print("| Sistema de Questionário de Satisfação |")
      print("-" * 41 + "\n")
      print("\n1. Responder ao Questionário")
      print("2. Sair")
      opcao = input("\nEscolha uma opção: ")

      if opcao == "1":
          respostas = apresentar_questionario()
          exportar_resultados(respostas)
      elif opcao == "2":
          print("Obrigado por usar o sistema!")
          print("Encerrando o sistema...")
          break
      else:
          print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
  main()
