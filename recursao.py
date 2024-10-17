# 1. Contagem de Dígitos em um Número: Crie uma função recursiva que receba
# um número inteiro positivo e retorne o número de dígitos desse número.
# contar_digitos(12345) # Saída: 5

def contar_digitos(n):
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)


resultado = contar_digitos(12345)
print("Número de dígitos:", resultado)  # Saída: 5

#2. Somar Elementos de uma lista: Escreva uma função recursiva que receba
#uma lista de números inteiros e retorne a soma de todos os seus elementos.
#soma_lista([1, 2, 3, 4, 5]) # Saída: 15

def soma_lista(lista):
    if not lista:
        return 0
    return lista[0] + soma_lista(lista[1:])


resultado = soma_lista([1, 2, 3, 4, 5])
print("Soma dos elementos:", resultado)  # Saída: 15


# 3. Verificar Palíndromo: Desenvolva uma função recursiva que verifique se uma
#palavra é um palíndromo (se a palavra lida de trás para frente é a mesma).
#verificar_palindromo("radar") # Saída: True
#verificar_palindromo("python") # Saída: False

def verificar_palindromo(palavra):
    # Caso base: se a palavra tem 0 ou 1 caracteres, é um palíndromo
    if len(palavra) <= 1:
        return True
    # Verifica se o primeiro e o último caracteres são iguais
    if palavra[0] != palavra[-1]:
        return False
    # Chamada recursiva: verifica a substring sem os extremos
    return verificar_palindromo(palavra[1:-1])

# Exemplos de uso
resultado1 = verificar_palindromo("radar")
resultado2 = verificar_palindromo("python")

print("Radar é um palíndromo?", resultado1)  # Saída: True
print("Python é um palíndromo?", resultado2)  # Saída: False


#4. Desenhar um Triângulo de Asteriscos: Implemente uma função recursiva
#que desenhe um triângulo de asteriscos com n linhas. Cada linha deve conter um
#número de asteriscos igual ao número da linha.
#desenhar_triangulo(3)
#Saída:
#*
#**
#***

def desenhar_triangulo(n, linha=1):
    if linha > n:
        return
    print('*' * linha)
    desenhar_triangulo(n, linha + 1)

# Exemplo de uso
desenhar_triangulo(3)


