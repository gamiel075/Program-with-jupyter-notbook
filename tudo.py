import pandas as pd

# Vamos criar um DataFrame de exemplo
dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'Pontuação': [85, 92, 78, 89]
}

df = pd.DataFrame(dados)

# Classificar o DataFrame com base na coluna 'Pontuação' em ordem decrescente (do maior para o menor)
df_ranking = df.sort_values(by='Pontuação', ascending=False)

# Mostrar o DataFrame classificado em forma de ranking
print(df_ranking)


aluno = {'gabriel': 20,'miguel' :25, 'rafael':16}
alunos = ['gabriel','rafael','daniel','miguel']

alunos.remove('gabriel')  #
alunos.append('muriel')


alunos.extend(['jhon','jack'])
alunos.insert(0,'Gabriel')

print(alunos) # saida = ['Gabriel','rafael', 'daniel', 'miguel', 'muriel', 'jhon', 'jack']



#forma de listar um dicionário

carros = []

for i in range(3):
    carro = {}
    carro['nome'] = input('Qual o nome do carro? ')
    carro['motor'] = input('Qual o motor do carro? ')
    carro['valor'] = int(input('Qual o seu valor? '))
    carros.append(carro)

print(carros)

#forma de listar uma lista

#mercado2 = []
#for i in range(3):
    #nome=input('digite o nome do item')
    #quantidade =int(input('digite a quantidade do item'))
    #valor = float(input('digite o valor do item'))
    #mercado2.append([nome,quantidade, 'R$'+ valor ])

compra = [['carnes',25.50] , ['frutas',15.70] , ['verduras',12.00] , ['legumes',10]]
valor_total = compra[0][1] + compra[2][1]
print(valor_total) #saida= 37.5


