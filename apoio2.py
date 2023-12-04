
from colorama import Fore, Back , Style , init

#formula

def a ():

    Preço_atacado = float(input('digite o valor unitário do produto no ataacdo'))
    Preço_venda = float(input('digite  o valor da venda'))
    Qtd_atacado = float(input('digite  a quantidade de compra no atacado'))
    qtd_vendas = float(input('digite  a quatidade de vendas projetadas'))
    print('--' * 20)
    fornecedor = Preço_atacado * Qtd_atacado
    venda = Preço_venda * qtd_vendas
    Lucro = venda - fornecedor
    print('seu lucro é de :')
    print(Lucro)

    return Lucro , fornecedor


def b(Lucro,fornecedor):

    porcento0 = fornecedor / 10  
    porcento1 = porcento0 * 5
    porcento2 = porcento0 * 10
    porcento3 = porcento0 * 20
    porcento4 = porcento0 * 30


       

    if(Lucro <= porcento1 ):
        print(Fore.RED + 'Status Negativo')

    elif(Lucro > porcento1 and Lucro < porcento2):
        print(Fore.YELLOW + 'Status regular')
        
    elif(Lucro > porcento2 and Lucro < porcento3):
         print(Fore.BLUE + 'status positivo') 
          
    elif(Lucro > porcento3 and Lucro < porcento4):
        print(Fore.GREEN + 'excelente') 



resulta = a()
b(*resulta)






    




    
   


   


    


