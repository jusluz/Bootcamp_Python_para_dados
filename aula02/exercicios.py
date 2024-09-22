# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num_01 = int(input('Digite um numero: '))
num_02 = int(input('Digite outro numero: '))
total = num_01 + num_02

print(total)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num = int(input('Digite um numero: '))
resto = num % 5

print(resto)

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
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação

