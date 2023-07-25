"""
aprimoramento do "challenge_2_bank_operations_1.py"
utilizando "funções" para otimização

FEITO       - separar em funções (saque, depósito e extrato);
FEITO       * função saque: argumentos apenas por nome (keyword only) - ex: saldo=saldo, valor=valor;
FEITO            ~ sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques;
FEITO            ~ sugestão de retorno: saldo, extrato;
FEITO       * função depósito: argumentos apenas por posição (positional only)
FEITO           ~ sugestão de argumentos: saldo, valor, extrato;
FEITO           ~ sugestão de retorno: saldo e extrato;
FEITO       * função extrato: argumentos por posição e por nome (positional only e keyword only)
FEITO           ~ argumentos posicionais: saldo;
FEITO           ~ argumentos nomeados: extrato;
    
- criar duas novas: usuário (cliente); conta corrente (vincular com usuário);
FEITO       * usuário;
FEITO           ~ armazenar usuários em uma lista - composto por nome, data de nascimento, CPF e endereço;
FEITO               ~ endereço é uma string com formato "logradouro, nº - bairro - cidade/sigla estado";
FEITO               ~ CPF: armazenar somente os números;
FEITO               ~ NÃO pode ser possível cadastrar dois usuários com CPFs iguais;
* conta-corrente - composta por agência, número da conta e usuário.
    ~ o número da conta é sequencial, iniciando em 1;
    ~ o número da agência é fixo: "0001";
    ~ o usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário;

dica: para vincular um usuário a uma conta filtre a lista de usuários buscando o número do CPF informado para
cada usuário da lista - se não encontrar um usuário, não pode criar uma conta (não pode haver contas sem usuários)
"""

menu = '''
INFORME A OPÇÃO DESEJADA:

[D] DEPOSITAR
[S] SACAR
[E] EXTRATO

[C] CADASTRAR CLIENTE
[L] LISTAR CLIENTES
[P] PROCURAR POR CLIENTE

[N] CADASTRAR CONTA
[M] LISTAR CONTAS

[Q] SAIR

>> '''

cadastro_usuario = {
"12345678910": {"nome": "OBI-WAN", "nascimento": "01-01-1974", "logradouro": "<logradouro>", "num_casa": "<num casa>","bairro": "<bairro>","cidade": "<cidade>","estado": "<estado-sigla>"},
"98765432110": {"nome": "ANAKIN", "nascimento": "01-01-1974", "logradouro": "<logradouro>", "num_casa": "<num casa>","bairro": "<bairro>","cidade": "<cidade>","estado": "<estado-sigla>"},
"12345678911": {"nome": "LEIA", "nascimento": "01-01-1974", "logradouro": "<logradouro>", "num_casa": "<num casa>", "bairro": "<bairro>", "cidade": "<cidade>", "estado": "<estado-sigla>"},
"98765432111": {"nome": "PADMÉ", "nascimento": "01-01-1974", "logradouro": "<logradouro>", "num_casa": "<num casa>", "bairro": "<bairro>", "cidade": "<cidade>", "estado": "<estado-sigla>"}
}
cadastro_conta = {
"12345678910": {"agencia": "0001", "conta": 1, "usuario": "12345678910"},
"98765432110": {"agencia": "0001", "conta": 2, "usuario": "98765432110"},
"12345678911": {"agencia": "0001", "conta": 3, "usuario": "12345678911"},
"98765432111": {"agencia": "0001", "conta": 4, "usuario": "98765432111"},
}

LIMITE_SAQUES = 3
acumulador_valor_saque = 0
numero_saques = 0
saldo = 0
limite = 500
extrato = ""

excedeu_LIMITE_SAQUES = f"[!] EXCEDE O LIMITE DE {LIMITE_SAQUES} SAQUES DIÁRIOS"
excedeu_limite = f"[!] VOCÊ EXCEDEU O LIMITE DIÁRIO DE R$ {limite:.2f}."
nao_possui_saldo = "[!] VOCÊ NÃO POSSUI SALDO SUFICIENTE"
valor_abaixo_zero = "[!] INFORME UM VALOR ACIMA DE R$ 0,00\n"
saldo_e = ">> O SALDO ATUAL É: R$ "
operacao_nao_permitida = "[!] OPERAÇÃO NÃO PERMITIDA\n"
operacao_permitida = "\n>> OPERAÇÃO BEM SUCEDIDA!\n"

def fdeposito(saldo, extrato, valor_deposito, /):
    
  if valor_deposito >= 0:
    saldo += valor_deposito
    extrato += (f"> DEPÓSITO:\tR$ {valor_deposito:.2f} (+)\n")
    print(f"{operacao_permitida}{saldo_e}{saldo:.2f}")

  else:
    print(f"{valor_abaixo_zero}")

  return saldo, extrato
def fsaque(*, valor_saque, limite, saldo, extrato):
  
  global acumulador_valor_saque
  global numero_saques

  validacao_1 = (valor_saque + acumulador_valor_saque) <= limite
  validacao_2 = numero_saques < LIMITE_SAQUES
  validacao_3 = (saldo - valor_saque) >= 0
  
  if validacao_1 == False and validacao_3 == True:
    print(f"\n{operacao_nao_permitida}{excedeu_limite}\n")

  if validacao_2 == False:
    print(f"\n{operacao_nao_permitida}{excedeu_LIMITE_SAQUES}\n")

  if validacao_3 == False:
    print(f"\n{operacao_nao_permitida}{nao_possui_saldo}\n")

  # validacao_1 - só pode realizar R$ X em saques (tanto unitário, quanto somatório)
  # validacao_2 - só pode realizar n operações "por dia"
  # validacao_3 - validação de saldo acima de R$ 0,00 ou se saque não deixa saldo negativo
  elif validacao_1 and validacao_2 and validacao_3:
    extrato += (f"> SAQUE:\tR$ {valor_saque:.2f} (-)\n")
    saldo -= valor_saque
    acumulador_valor_saque += valor_saque
    numero_saques += 1

  print(f"{saldo_e}{saldo:.2f}")

  return saldo, extrato
def fextrato(saldo, /, *, extrato):
    
    print(f"""
=========== EXTRATO ===========
===      movimentações      ===

{extrato}

> SALDO: R$ {saldo:.2f}
===============================""")
def cadastrar_usuario(cpf):
    
  if cadastro_usuario.get(cpf):
    print(f"\n>> CLIENTE {cpf} JÁ POSSUI CADASTRO")
    nome = cadastro_usuario[cpf]["nome"]
    nascimento = cadastro_usuario[cpf]["nascimento"]
    print(f"\n>> NOME: {nome}\n>> NASCIMENTO: {nascimento}")

  else:
    nome = input("NOME: ").upper()
    nascimento = input("NASCIMENTO: ")
    logradouro = input("RUA: ").upper()
    num_casa = int(input("NÚMERO: "))
    bairro = input("BAIRRO: ").upper()
    cidade = input("CIDADE: ").upper()
    estado = input("ESTADO (SIGLA): ").upper()
    cadastro_usuario[cpf] = {"nome": nome, "nascimento": nascimento, "logradouro": logradouro, "num_casa": num_casa, "bairro": bairro, "cidade": cidade, "estado": estado}
def listar_usuario():

  for usuario in cadastro_usuario:
    print(f">> NOME: {cadastro_usuario[usuario]['nome']} - CPF: {usuario}\n>> DATA DE NASCIMENTO: {cadastro_usuario[usuario]['nascimento']}\n")
def procurar_usuario():
    
  usuario_procurado = input(">> INFORME O 'CPF': ")
  cpf = usuario_procurado
  if cpf in cadastro_usuario:
    valor_encontrado = cadastro_usuario[cpf]
    print(f"\n>> USUÁRIO ENCONTRADO\n>> NOME: {valor_encontrado['nome']}\n>> DATA DE NASCIMENTO: {valor_encontrado['nascimento']}")
  else:
    print(f"\n>> USUÁRIO NÃO ENCONTRADO\n>> NÃO EXISTE CLIENTE CADASTRADO COM O CPF {cpf}")
def cadastrar_conta(cpf):
    
  if cadastro_conta.get(cpf):
    print(f"\n[!] CLIENTE {cpf} JÁ POSSUI UMA CONTA")
    nome = cadastro_usuario[cpf]["nome"]
    nascimento = cadastro_usuario[cpf]["nascimento"]
    agencia = cadastro_conta[cpf]["agencia"]
    conta = cadastro_conta[cpf]["conta"]
    print(f"\n>> NOME: {nome}\n>> NASCIMENTO: {nascimento}\n>> AGÊNCIA: {agencia} // CONTA: {conta}")
    
    opcao = input("\n>> DESEJA CADASTRAR UMA NOVA CONTA PARA ESTE USUÁRIO? [S/N]\n>> ").upper()
    
    if opcao == "N":
      return
    
    elif opcao == "S":
      return
      # implementar código para adicionar conta
      
  else:
    return
    # implementar código para adicionar conta
def listar_contas():
    
  for conta in cadastro_conta:
    print(f">> AGÊNCIA: {cadastro_conta[conta]['agencia']} - CONTA: {cadastro_conta[conta]['conta']}\n>> CPF: {conta}\n")

while True:
    
  opcao = input(menu).upper()

  if opcao == "Q":
    print('>> SAINDO DO SISTEMA...\n')
    break

  elif opcao == "D":
    print('=== DEPÓSITO ===\n')
    valor_deposito = float(input(">> INFORME O VALOR DO DEPÓSITO: R$ "))
    saldo, extrato = fdeposito(saldo, extrato, valor_deposito)
    
  elif opcao == "S":
    print('=== SAQUE ===\n')
    valor_saque = float(input(">> INFORME O VALOR DO SAQUE: R$ "))
    saldo, extrato = fsaque(valor_saque=valor_saque, limite=limite, extrato=extrato, saldo=saldo)

  elif opcao == "E":
    print('=== EXTRATO ===\n')
    fextrato(saldo, extrato=extrato)

  elif opcao == "C":
    print("=== CADASTRAR NOVO USUÁRIO ===\n")
    cpf = input("INFORME O CPF: ")
    cadastrar_usuario(cpf)

  elif opcao == "L":
    print("=== LISTAR CLIENTES ===\n")
    listar_usuario()

  elif opcao == "P":
    print("=== PROCURAR POR CLIENTE ===\n")
    procurar_usuario()

  elif opcao == "N":
    print("=== CADASTRAR NOVA CONTA ===\n")
    cpf = input("INFORME O CPF: ")
    cadastrar_conta(cpf)
    
  elif opcao == "M":
    print("=== LISTAR CONTAS ===\n")
    listar_contas()

  else:
      print("""
[!] COMANDO DESCOHECIDO
[!] SELECIONE UMA OPÇÃO VÁLIDA""")
