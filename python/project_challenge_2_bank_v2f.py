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

[d] DEPOSITAR
[s] SACAR
[e] EXTRATO

[c] CADASTRAR CLIENTE
[l] LISTAR CLIENTES
[p] PROCURAR POR CLIENTE

[q] SAIR

>> '''

cadastro_usuario = {
    "12345678910": {"nome": "OBI-WAN",
                    "nascimento": "01-01-1974",
                    "logradouro": "<logradouro>", 
                    "num_casa": "<num casa>",
                    "bairro": "<bairro>",
                    "cidade": "<cidade>",
                    "estado": "<estado-sigla>"},

    "98765432110": {"nome": "ANAKIN", 
                    "nascimento": "01-01-1974",
                    "logradouro": "<logradouro>", 
                    "num_casa": "<num casa>",
                    "bairro": "<bairro>",
                    "cidade": "<cidade>",
                    "estado": "<estado-sigla>"},

    "12345678911": {"nome": "LEIA",
                    "nascimento": "01-01-1974",
                    "logradouro": "<logradouro>",
                    "num_casa": "<num casa>",
                    "bairro": "<bairro>",
                    "cidade": "<cidade>",
                    "estado": "<estado-sigla>"},
    "98765432111": {"nome": "PADMÉ",
                    "nascimento": "01-01-1974",
                    "logradouro": "<logradouro>",
                    "num_casa": "<num casa>",
                    "bairro": "<bairro>",
                    "cidade": "<cidade>",
                    "estado": "<estado-sigla>"}
}

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

def fdeposito(saldo, extrato, valor_deposito, /):
    
    if valor_deposito >= 0:
        saldo += valor_deposito
        extrato += (f"> Depósito:\tR$ {valor_deposito:.2f} (+)\n")
        print(f"\nOperação bem sucedida!\nO saldo atual é: R$ {saldo:.2f}")

    else:
        print("Informe um valor acima de R$ 0,00")

    return saldo, extrato
def fsaque(*, valor_saque, limite, saldo, extrato):
    
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
def cadastrar_usuario(cpf):
    
    if cadastro_usuario.get(cpf):
        print(f"Cliente {cpf} já possui cadastro")

    else:
        nome = input("Nome: ").upper()
        nascimento = input("Nascimento: ")
        logradouro = input("Rua: ").upper()
        num_casa = int(input("Número: "))
        bairro = input("Bairro: ").upper()
        cidade = input("Cidade: ").upper()
        estado = input("Estado (sigla): ").upper()
        cadastro_usuario[cpf] = {"nome": nome, "nascimento": nascimento, "logradouro": logradouro, "num_casa": num_casa, "bairro": bairro, "cidade": cidade, "estado": estado}

    nome = cadastro_usuario[cpf]["nome"]
    nascimento = cadastro_usuario[cpf]["nascimento"]
    print(nome, nascimento)
def listar_usuario():

    for usuario in cadastro_usuario:
        print(f"NOME: {cadastro_usuario[usuario]['nome']} - CPF: {usuario}\nDATA DE NASCIMENTO: {cadastro_usuario[usuario]['nascimento']}\n")
def procurar_usuario():
    
    usuario_procurado = input("Informe o CPF procurado: ")
    cpf = usuario_procurado
    if cpf in cadastro_usuario:
        valor_encontrado = cadastro_usuario[cpf]
        print(f"\nUSUÁRIO ENCONTRADO\nNOME: {valor_encontrado['nome']}\nDATA DE NASCIMENTO: {valor_encontrado['nascimento']}")
    else:
        print(f"\nUSUÁRIO NÃO ENCONTRADO\nNÃO EXISTE CLIENTE CADASTRADO COM O CPF {cpf}")

while True:
    
    opcao = input(menu).lower()

    if opcao == "q":
        print('SAINDO DO SISTEMA...\n')
        break

    elif opcao == "d":
        print('DEPÓSITO\n')
        valor_deposito = float(input("Informe o valor do depósito: R$ "))
        saldo, extrato = fdeposito(saldo, extrato, valor_deposito)
    
    elif opcao == "s":
        print('SAQUE\n')
        valor_saque = float(input("Informe o valor do saque: R$ "))
        saldo, extrato = fsaque(valor_saque=valor_saque, limite=limite, extrato=extrato, saldo=saldo)

    elif opcao == "e":
        print('EXTRATO\n')
        fextrato(saldo, extrato=extrato)

    elif opcao == "c":
        print("CADASTRAR NOVO USUÁRIO\n")
        cpf = input("Digite o CPF do cliente: ")
        cadastrar_usuario(cpf)

    elif opcao == "l":
        print("LISTAR CLIENTES\n")
        listar_usuario()

    elif opcao == "p":
        print("PROCURAR POR CLIENTE\n")
        procurar_usuario()
    
    else:
        print("""
Comando desconhecido
Selecione uma operação válida""")
