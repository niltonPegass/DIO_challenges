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
* usuário;
    ~ armazenar usuários em uma lista - composto por nome, data de nascimento, CPF e endereço;
        ~ endereço é uma string com formato "logradouro, nº - bairro - cidade/sigla estado";
        ~ CPF: armazenar somente os números;
        ~ NÃO pode ser possível cadastrar dois usuários com CPFs iguais;
* conta-corrente - composta por agência, número da conta e usuário.
    ~ o número da conta é sequencial, iniciando em 1;
    ~ o número da agência é fixo: "0001";
    ~ o usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário;

dica: para vincular um usuário a uma conta filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista - se não encontrar um usuário, não pode criar uma conta (não pode haver contas sem usuários)
"""

menu = '''
INFORME A OPÇÃO DESEJADA:

[d] DEPOSITAR
[s] SACAR
[e] EXTRATO
[q] SAIR

>> '''

# definição de condições e limites
LIMITE_SAQUES = 3
acumulador_valor_saque = 0
numero_saques = 0
saldo = 0
limite = 500
extrato = ""

# mensagens para operações do usuário fora das 
# condições e limites inicialmente estabelecidos
excedeu_LIMITE_SAQUES = f"[!] Excede o limite de {LIMITE_SAQUES} saques diários."
excedeu_limite = f"[!] Você excedeu o limite diário de R$ {limite:.2f}."
nao_possui_saldo = "[!] Você não possui saldo suficiente."
operacao_nao_permitida = "Operação não permitida:\n"

def fdeposito(saldo, extrato, valor_deposito, /): # argumentos posicionais antes da barra
    

    if valor_deposito >= 0:
        saldo += valor_deposito
        extrato += (f"> Depósito:\tR$ {valor_deposito:.2f} (+)\n")
        print(f"\nOperação bem sucedida!\nO saldo atual é: R$ {saldo:.2f}")

    else:
        print("Informe um valor acima de R$ 0,00")

    return saldo, extrato
def fsaque(*, valor_saque, limite, saldo, extrato): # argumentos nomeados depois do asteristco
    
    global acumulador_valor_saque
    global numero_saques

    validacao_1 = valor_saque + acumulador_valor_saque <= limite
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

        extrato += (f"> Saque:\tR$ {valor_saque:.2f} (-)\n")
        saldo -= valor_saque
        acumulador_valor_saque += valor_saque
        numero_saques += 1

    print(f"O saldo atual é: R$ {saldo:.2f}")

    return saldo, extrato
def fextrato(saldo, /, *, extrato):
    
    print(f"""
=========== EXTRATO ===========
===      movimentações      ===

{extrato}

> SALDO: R$ {saldo:.2f}
===============================""")

while True:
    
    opcao = input(menu).lower()

    if opcao == "q":
        print('SAINDO DO SISTEMA...\n')
        break

    elif opcao == "d":
        print('DEPÓSITO')
        valor_deposito = float(input("Informe o valor do depósito: R$ "))
        saldo, extrato = fdeposito(saldo, extrato, valor_deposito)
    
    elif opcao == "s":
        print('SAQUE')
        valor_saque = float(input("Informe o valor do saque: R$ "))
        saldo, extrato = fsaque(valor_saque=valor_saque, limite=limite, extrato=extrato, saldo=saldo)

    elif opcao == "e":
        print('EXTRATO')
        fextrato(saldo, extrato=extrato)
    
    else:
        print("""
Comando desconhecido
Selecione uma operação válida""")
