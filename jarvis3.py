while True:
    print("=== JARVIS: MISSOES ===")
    print("1 - Iniciar missão")
    print("2 - Desligar")

    opcao = input("Escolha: ")

    # Complete a lógica aqui

    if opcao == "1":
      pontos = 0

      print("Qual o maior oceano do mundo?")
      resposta_usuario = input("Responda: ")


      if resposta_usuario  == "Oceano pacífico":
        print("Correto!! Você ganhou 3 pontos.")
        pontos += 3
        
      else:
        print("Incorreto.")

    ##################################################    
               
      print("Qual média de qi no Brasil?")
      resposta_usuario = input("Responda: ")

      if resposta_usuario == "entre 83 e 98 pontos":
        print("Correto!! Você ganhou 3 pontos.")
        pontos += 3
        
      else:
        print("Incorreto.")

    ##################################################      

      print("Diga 3 países que são potência?")
      resposta_usuario = input("Responda: ")

      if resposta_usuario == "Estados unidos, Japão e Russia":
         print("Correto!! Você ganhou 3 pontos.")
         pontos += 3
        
      else:
        print("Incorreto.")   

      total = pontos 

      print(f"Total de pontos: {total}") 

      break  

      
    



