#contar dinheiro no caixa eletronico

valor = int(input('Digite o valor que gostaria sacar em R$ :'))
cedula = 100
totalcedula = 0 
while True:
    if valor >= cedula:
        valor = valor - cedula
        totalcedula = totalcedula + 1
    else:
        print(f'Total de {totalcedula} cédulas de R${cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        totalcedula = 0 
        if valor == 0:
            break