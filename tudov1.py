carros = []

for i in range(3):
    carro = {}
    carro['nome'] = input('Qual o nome do carro? ')
    carro['motor'] = input('Qual o motor do carro? ')
    carro['valor'] = int(input('Qual o seu valor? '))
    carros.append(carro)

print(carros)
