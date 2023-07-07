menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''

LIMITE_SAQUES = 3
numero_saques = 0
saldo = 0
limite = 500
extrato = ""

acumulador_valor_saque = 0
operacoes_realizadas = 0

excedeu_limite = f"Você excedeu o limite diário de R$ {limite:.2f}.\n"
excedeu_LIMITE_SAQUES = f"Excede o limite de {LIMITE_SAQUES} saques diários.\n"
operacao_nao_permitida = "Operação não permitida.\n"

while True:
    
    opcao = input(menu)

    if opcao == "d":
      print("DEPÓSITO\n")

      valor_deposito = input("Informe o valor do depósito: R$ ")
      valor_deposito = float(valor_deposito)
      
      if valor_deposito > 0:
        extrato += f"> Depósito de R$ {valor_deposito:.2f} (+)\n"
        saldo += valor_deposito
        print(saldo)
      else:
        print("Informe um valor acima de R$ 0,00")

    elif opcao == "s":
      print("SAQUE\n")

      valor_saque = input("Informe o valor do saque: R$ ")
      valor_saque = float(valor_saque)

      validacao_1 = operacoes_realizadas < LIMITE_SAQUES
      validacao_2 = valor_saque + acumulador_valor_saque <= limite
      validacao_3 = saldo > 0

      if validacao_1 == False:
          print(f"{excedeu_LIMITE_SAQUES}{operacao_nao_permitida}")
      if validacao_2 == False:
          print(f"{excedeu_limite}{operacao_nao_permitida}")

      if validacao_1 and validacao_2 and validacao_3:
        
        extrato += f"> Saque de R$ {valor_saque:.2f} (-)\n"
        saldo -= valor_saque
        acumulador_valor_saque += valor_saque
        operacoes_realizadas += 1

      print(f"O saque acumulado é: R$ {acumulador_valor_saque:.2f}")
      print(f"O saldo atual é: R$ {saldo:.2f}")
    
    elif opcao == "e":
      print(f"""
=========== EXTRATO ===========
===      movimentações      ===

{extrato}

> SALDO: R$ {saldo}
===============================""")

    elif opcao == "q":
      break

    else:
      print("""
Comando desconhecido
Selecione uma operação válida
    """)
