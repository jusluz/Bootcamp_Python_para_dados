# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num_01 = int(input('Digite um numero: '))
num_02 = int(input('Digite outro numero: '))
total = num_01 + num_02

print('Total: {}'.format(total))

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num = int(input('Digite um numero: '))
resto = num % 5

print('O valor do resto é ', resto)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num01 = float(input('Informe um numero: '))
num02 =  float(input('Nos informe outro numero: '))
resultado = num01 * num02

print(resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num_int01 = int(input('Digite um numero: '))
num_int02 = int(input('Digite outro numero: '))
divisao_int = num_int01 //  num_int02

print(divisao_int)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num_usuario = int(input('Digite um numero'))
raiz_quadrada_de_um_numero = num_usuario * num_usuario

print(f'A raiz quadrada de {num_usuario} é {raiz_quadrada_de_um_numero}.')

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
num_fl01 = float(input('Digite um numero: '))
num_fl02 = float(input('Digite outro numero: '))
add = num_fl01 + num_fl02

print(add)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num_fl03 = float(input('Digite um numero: '))
num_fl04 = float(input('Digite outro numero: '))
total_fl = (num_fl03 + num_fl04)
media_fl = total_fl / 2

print(media_fl) 

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = int(input('Digite o valor da base: '))
expoente = int(input('Digite o valor do expoente: '))
potencia = base ** expoente

print(potencia)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
graus_celsius =  int(input('Digite o valor da temperatura: '))
graus_fahrenheit = (graus_celsius * 9/5) + 32
graus_fahrenheit_2 =  round(graus_celsius * 1.8, 2) + 32

print(graus_fahrenheit)
print(graus_fahrenheit_2)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
pi = 3.1415
raio = float(input('Digite o valor do raio: '))

area = pi * (raio ** 2)

print(area)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
falando_alto = input('Digite uma frase: ')

print(falando_alto.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = input('Digite seu nome completo: ')
nome_completo = nome_completo.lower()

print(nome_completo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input('Digite uma frase: ')
frase = frase.strip()

print(frase)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input('Digite uma data no formato dd/mm/aaaa: ')
data = data.split('/')

print(f'Dia: {data[0]}\nMes: {data[1]}\nAno: {data[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string1 = input('Digite a primeira string: ')
string2 = input('Digite a segunda string: ')

string3 = string1 + string2
print(string3)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao1 = input('Digite a primeira expressão booleana (True ou False): ')
expressao2 = input('Digite a segunda expressão booleana (True ou False): ')

expressao_and = expressao1 and expressao2
print(expressao2)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
expressao3 = input('Digite o primeiro valor booleano (True ou False): ')
expressao3 = expressao3.capitalize()

expressao4 = input('Digite o segundo valor: booleano (True ou False): ')
expressao4 = expressao4.capitalize()

expressao_or = expressao3 or expressao4

print(expressao_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor_bool = input('Digite um valor entre True ou False: ')
valor_bool = valor_bool.capitalize()
print('Voce digitou {}'.format(valor_bool))

inverte_valor_bool =  valor_bool != valor_bool
print(f'O valor invertido ficou em {inverte_valor_bool}')

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
'São números iguais' if num1 == num2 else 'Não são iguais'

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num03 = int(input('Digite o primeiro número: '))
num04 = int(input('Digite o segundo número: '))
'São números diferentes' if num03 != num04 else 'Não são diferentes'

# #### try-except e if

# 21: Conversor de Temperatura
try:
    temperatura = float(input('Digite a temperatura em Celsius: '))
    if type(temperatura) == float:
    #if isinstance(temperatura,float):
        temperatura_fahrenheit = (temperatura * 9/5) + 32
        print(f'A temperatura em Fahrenheit é {temperatura_fahrenheit}°F')

except ValueError:
    print('Erro: valor inválido')

# 22: Verificador de Palíndromo
try:
    palavra = input('Digite uma palavra: ')
    palavra = palavra.lower()
    if isinstance(palavra, str):
        palavra_invertida = palavra[::-1]
        if palavra == palavra_invertida:
            print(f'A palavra {palavra} é um palíndromo')
        else:
            print(f'A palavra {palavra} não é um palíndromo')
except ValueError:
    print('Erro: valor inválido')

# 23: Calculadora Simples
try:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operador = input('Digite o operador (+, -, *, /): ')
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
    else:
        print('Erro: operador inválido')
    print(f'O resultado é {resultado}')
except ValueError:
    print('Erro: valor inválido')

# 24: Classificador de Números
try:
    num = float(input('Digite um número: '))
    if isinstance(num, float):
        if num > 0:
            if num % 2 == 0:
                print(f'O número {num} é par e positivo.')
            else:
                print(f'O número {num} é impar e positivo.')
        elif num < 0:
            if num % 2 !=0:
                print(f'O número {num} é impar e negativo')
            else:
                print(f'O número {num} é par e negativo')
        else:
            print(f'O número {num} é zero')
except ValueError:
    print('Erro: valor inválido')

# 25: Conversão de Tipo com Validação
try:
    num = input('Digite uma lista de numeros separados por vírgula: ')
    lista_numeros = [int(i) for i in num.split(',')]
    print(f'A lista de números é {lista_numeros}')

except ValueError:
    print('Favor, verificar se todos os elementos digitados são numéricos')
