"""
aprimoramento do "challenge_2_bank_operations_1.py"
utilizando "função" para otimização

definições e regras:
- separar em funções (saque, depósito e extrato);
	* função saque: argumentos apenas por nome (keyword only) - ex: saldo=saldo, valor=valor;
		~ sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques;
		~ sugestão de retorno: saldo, extrato;
	* função depósito: argumentos apenas por posição (positional only)
		~ sugestão de argumentos: saldo, valor, extrato;
		~ sugestão de retorno: saldo e extrato;
	* função extrato: argumentos por posição e por nome (positional only e keyword only)
		~ argumentos posicionais: saldo;
		~ argumentos nomeados: extrato;
		
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
