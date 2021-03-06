'''
Descrição
Escreva um programa que irá receber duas entradas: uma sequencia de caracteres e um único caractere e irá contar quantas vezes o caractere aparece na sequencia. Você deve escrever uma função que irá receber como parâmetros a sequencia e o caractere, e retornar o número de ocorrências pedido. No código principal do programa, faça a leitura dos dados de entrada (input's), chame a sua função para contar o número de ocorrências, e em seguida imprima o resultado pedido.

OBS: Não é permitido o uso do .count() para realizar a contagem. 

DICA: A ideia é criar uma função que faça a mesma coisa que o .count(), portanto você pode usar o .count() para comparar os seus resultados e validar a sua função. Para fazer a contagem, faça um laço (for ou while) iterando sobre a sequência e criei um contador para guardar quantas vezes o caractere foi encontrado.

Formato de entrada

A entrada conterá duas strings, sendo a primeira a sequências de caracteres e a segunda o caractere que deve ser buscado.
'''

frase = str(input()).upper()
procurar = str(input()).upper()

tamanho = len(frase)
contador = 0

for x in range(0,tamanho):
    if frase[x] == procurar:
        contador = contador + 1
if contador > 0:
    print("O caractere buscado ocorre", contador, "vezes na sequencia.")
else:
    print("Caractere nao encontrado.")