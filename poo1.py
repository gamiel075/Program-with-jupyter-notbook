


def criar_tv(ano_tv,marca_tv,preço_tv):

    tv = { 'ano': ano_tv,'marca': marca_tv,'preço':preço_tv}
    return tv

def aumentar_preço(tv,valor): #função colocada em seguida ver *obs
    tv['preço'] += valor

def diminuir_preço(tv,valor): #função colocada em seguida ver *obs
    tv['preço'] -= valor

def consultar_preço(tv):

    return f"a tv {tv['marca']} custa {tv['preço']}"


###################################################

tv4 = criar_tv(2024,'lg',1500)
print(tv4)#saida = {'ano': 2024, 'marca': 'lg', 'preço': 1500}


print(tv4.keys())
#saida: dict_keys(['ano', 'marca', 'preço'])


###################################################
aumentar_preço(tv4,100)
print(tv4['preço'])
#saida = 1600
################################################
diminuir_preço(tv4,300)
print(tv4['preço'])
#saida: 1300 
#################################################
consultar_preço(tvbSDKHDGHWGDWDGWDGQdg 

        

        

        



        


