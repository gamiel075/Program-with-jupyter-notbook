
class ContaBancaria:
    def __init__(self, nome_titular ,saldo_initial = 0):
    
        self.nome_titular = nome_titular
        self.saldo =  saldo_initial
    
    def depositar(self,valor):
        self.saldo += valor
        print(f'Deposito de {valor}.Novo saldo de {self.saldo} na conta de {self.nome_titular}')

    def sacar(self,valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print(f'saque de {valor}.Novo saldo de {self.saldo} na conta de {self.nome_titular} ' )
        else:
            print('saldo insuficiente para saque ')



minha_conta = ContaBancaria('gabriel',500)

minha_conta.depositar(500)
minha_conta.sacar(200)
minha_conta.sacar(900)

#################################################################

class Transação:

    def __init__ (self,produto,valor):
        
        self.produto = produto
        self.valor = valor

    def notafiscal (self):

        print('------' * 10)
        print(f'produto comprado: {self.produto}')
        print(f'Valor: {self.valor}')
       


compra = Transação('arrroz',20)  
compra.notafiscal()
##################################################################################
from colorama import Fore, Style


class Análise:

    def __init__(self, titulo_investimento , valor , data_retorno_meses ):

        self.titulo_investimento = titulo_investimento
        self.valor = valor
        self.data_retorno = data_retorno_meses

    def consulta (self):

        if(self.valor > 100000):
            print(Fore.RED + 'Investimento De Alto Risco')
        
        elif(self.valor > 80000 and self.valor <100000):
            print(Fore.YELLOW + 'Investimento de Médio Risco')
        
        elif(self.valor > 60000 and self.valor < 80000 ):
            print(Fore.BLUE + 'Investimento De Baixo Risco')

        elif(self.valor > 40000 and self.valor < 60000  ):
            print(Fore.GREEN + 'Investimento Seguro')



    def rendamensal(self):

        valor_porcento = 0

        if(self.valor > 100000):
            valor_porcento += 25
        
        elif(self.valor > 80000 and self.valor <100000):
            valor_porcento += 20
        
        elif(self.valor > 60000 and self.valor < 80000 ):
            valor_porcento += 15

        elif(self.valor > 40000 and self.valor < 60000  ):
            valor_porcento += 10
        
        return valor_porcento



    def calculoxtempo(self,valor_porcento):

        valor1 =   self.valor / 100
        valor2 = valor1 * valor_porcento
        valor3 = valor2 * self.data_retorno
        valor4 = self.valor + valor3

        print('------' * 10)
        print(f'O você receberá o equivalente á {valor2} mensamente por {self.data_retorno} meses')
        print(f'Sua renda será {valor4}')
        print('-----' * 10)

meu_investimento = Análise('ações lunitecnologi',65000,5)

meu_investimento.consulta()
result = meu_investimento.rendamensal()
meu_investimento.calculoxtempo(result)

##########################################################################################################
class Montador:

    def __init__(self,Nome_veículo,tipagem_veiculo, modelo_veículo):

        self.Nome_veículo = Nome_veículo
        self.tipagem_veiculo = tipagem_veiculo
        self.modelo_veículo = modelo_veículo


    def tipagem(self):

        geração1 = self.tipagem_veiculo
        
        geração2 = 'categoria:'

        if(geração1  == 2 ):
            geração_veiculo =  geração2 + 'primeira geração'

        elif( geração1 == 4):
            geração_veiculo= geração2 +'segunda geração'

        elif(geração1 == 6):
            geração_veiculo =  geração2 + 'terceira geração'

        elif(geração1 == 8):
            geração_veiculo = geração2 + 'quarta geração'


        print(self.Nome_veículo)
        print(geração_veiculo)
    
    def motor(self):
        
        if(self.modelo_veículo == 'yeager'):

            motor_veiculo = 'élétrico'
            corpo_véiculo = 'esportivo'
            especialidade_veículo = 'rápido e elegante'

            print(motor_veiculo)
            print(corpo_véiculo)
            print(especialidade_veículo)
        
        elif(self.modelo_veículo == 'smith'):
            
            motor_veiculo = 'á gas'
            corpo_véiculo = 'caminhão'
            especialidade_veículo = 'transporte de longas distancias'

            print(motor_veiculo)
            print(corpo_véiculo)
            print(especialidade_veículo)

            
        elif(self.modelo_veículo == 'silva'):

            motor_veiculo = 'á combustão'
            corpo_véiculo = 'carrocceria blindada'
            especialidade_veículo = 'terreno hostil'
            
        
            print(motor_veiculo)
            print(corpo_véiculo)
            print(especialidade_veículo)



        
        

meucarro = Montador('veron',4,'smith')
meucarro.tipagem()
meucarro.motor()

