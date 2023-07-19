from string import Template

# dicionário com os exemplos fornecidos no
# desafio usados no output para a resposta
cadastro_restaurante = {
    "MCDONALDS": {"nome": "Mc Donalds", "tempoEstimadoEntrega": 10},
    "KFC": {"nome": "KFC", "tempoEstimadoEntrega": 25},
    "BURGUERKING": {"nome": "Burguer King", "tempoEstimadoEntrega": 5},
    "GIRAFFAS": {"nome": "Giraffas", "tempoEstimadoEntrega": 35}
}
# leitura dos dados fornecidos para o usuário, e
# utilizados na condicional abaixo
nomeRestaurante = input("Digite o nome do restaurante: ")
tempoEstimadoEntrega = int(input("Digite o tempo de espera: "))

# método "get()" verifica se ja possui o elemento no dicionário
# caso já exista retorna o valor do dicionário e entra no "if" (já existe o 'elemento')
# caso não exista retorna "None" e cai no "else" e adicionamos o elemento
# sem fazer alguma sobreposição em outro previamente existente
if cadastro_restaurante.get(nomeRestaurante.upper().replace(" ", "")):
  print(f"Já existe o restaurante {nomeRestaurante} cadastrado")
else:
  cadastro_restaurante[nomeRestaurante.upper().replace(" ", "")] = {"nome": nomeRestaurante, "tempoEstimadoEntrega": tempoEstimadoEntrega}

# extração dos dados do dicionário para apresentar
# na resposta para o usuário
nomeRestaurante = cadastro_restaurante[nomeRestaurante.upper().replace(" ", "")]["nome"]
tempoEstimadoEntrega = cadastro_restaurante[nomeRestaurante.upper().replace(" ", "")]["tempoEstimadoEntrega"]

# saída do programa com a resposta na tela
template = Template("O restaurante $nome_restaurante entrega em $tempoEstimadoEntrega minutos")
mensagem_usuario = template.substitute(nome_restaurante=nomeRestaurante, tempoEstimadoEntrega=tempoEstimadoEntrega)
print(mensagem_usuario)

# adicionei os métodos .upper().replace(" ", "") para tratar os dados
# digitados e garantir que na busca não tenha a chance do que o usuário
# digitou não seja encontrado por diferenças de espaços e caracteres
