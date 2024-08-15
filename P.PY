# 

# nome = input("digite seu nome: ")
# cpf = input("digite seu CPF: ")
# endereço = input("digite seu endereço: ")
# email = input("digite seu email: ")
# telefone = input("digite seu telefone: ")

# cadastro = [nome, cpf, email, endereço, telefone]

# print("cadastro do cliente:")
# print("nome:",cadastro[0])
# print("email:",cadastro[1])
# print("cpf:",cadastro[1])


# comprar   um  produto



# produtos = ['celular', 'tv', 'computador']
# preços = [2999.90, 4999.90, 3999.90]

# print("produtos disponiveis: ")
# print("1.",produtos[0],  -  R$ ,precos[0])
# print("2.",produtos[1],  -  R$ ,precos[1])
# print("3.",produtos[2],  -  R$ ,precos[2])

# produtos = ['1 celular,3 computador']
# preços = ['2999.90, + 3999.90']
# print(valor total dos produto1 e produto3)


# DESAFIO2

cliente1= input('digite seu nome')
client1_idade= input('digite sua idade')

cliente2= input('digite seu nome')
cliente2_idade= (int(input ('digite sua idade')))


cliente3= input('digite seu nome')
cliente3_idade= int(input('digite sua idade'))

Quarto_cliente1= input('escolha os quarto("simples", "duplo" e "luxo".)').strip().lower()
Quarto_cliente2= input('escolha os quarto("simples", "duplo" e "luxo".)').strip().lower()
Quarto_cliente3= input('escolha os quarto("simples", "duplo" e "luxo".)').strip().lower()

dias_cliente1= int(input('escolha quantos dias'))
dias_cliente2= int(input('escolha quantos dias'))
dias_cliente3= int(input('escolha quantos dias'))

preço_simples= 100.00
preço_duplo= 150.00
preço_luxo= 250.00

if Quarto_cliente1 == 'simples':
    valor_cliente1= preço_simples * dias_cliente1
elif Quarto_cliente1 == 'duplo':
    valor_cliente1= preço_duplo * dias_cliente1
elif Quarto_cliente1 == 'luxo':
    valor_cliente1= preço_luxo * dias_cliente1
else:
    valor_cliente1=0

if Quarto_cliente2 == 'simples':
    valor_cliente2= preço_simples * dias_cliente2
elif Quarto_cliente2 == 'duplo':
    valor_cliente2= preço_duplo * dias_cliente2
elif Quarto_cliente2 == 'luxo':
    valor_cliente2= preço_luxo * dias_cliente2
else:
    valor_cliente2=0 

if Quarto_cliente3 == 'simples':
    valor_cliente3= preço_simples * dias_cliente3
elif Quarto_cliente3 == 'duplo':
    valor_cliente3= preço_duplo * dias_cliente3
elif Quarto_cliente3 == 'luxo':
    valor_cliente3= preço_luxo * dias_cliente3
else:
    valor_cliente3=0

print(f'\nresumo:')
print(f"cliente_1({cliente1})): R$ {valor_cliente1:.2f}")
print(f"cliente_2({cliente2})): R$ {valor_cliente1:.2f}")
print(f"cliente_3({cliente3})): R$ {valor_cliente1:.2f}") 
































































