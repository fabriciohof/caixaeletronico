#contar dinheiro no caixa eletronico

numero = int(input('Valor para sacar : '))

cem = int(numero / 100)
numero = numero - (cem*100)
    
cinquenta = int(numero/50)
numero = numero - (cinquenta*50)

dez = int(numero/10)
numero = numero - (dez*10)

cinco = int(numero/5)
numero = numero - (cinco*5)
    
print('Notas R$100,00 = ',cem)
print('Notas R$ 50,00 = ',cinquenta)
print('Notas R$ 10,00 = ',dez)
print('Notas R$  5,00 = ',cinco)