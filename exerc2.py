# Exercicio 1
numero = int(input('Numero: '))
if numero % 2 == 0:
    print(f' O numero {numero} é par')
else:
    print(f' O numero {numero} é impar')



# Exercicio 2
idade = int(input('Idade: '))

if idade >= 18:
    print('Você é adulto')
elif idade >= 12 and idade <= 17:
    print('Você é um adolecente')
elif idade < 11:
    print('Você é uma criança')
elif idade < 0:
    print('Você ainda não nasceu')

# Exercicio 3
usuario_correto = "gustavo"
senha_correta = "1234"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")

# Exercicio 4
x = float(input('Coordenada X: '))
y = float(input('Coordenada Y: '))

if x > 0 and y > 0:
    print('Ponto no quadrante 1')
elif x < 0 and y > 0:
    print('Ponto no quadrante 2')
elif x < 0 and y < 0:
    print('Ponto no quadrante 3')
elif x > 0 and y < 0:
    print('Ponto no quadrante 4')
else:
    print('Ponto na origem ou sobre um eixo')
