#contar dinheiro no caixa eletronico

valorSaque = int(input('Valor do saque: R$ '))
print('\n')

for nota in [100,50, 20, 10]:
    quantidade = valorSaque // nota
    valorSaque = valorSaque % nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')