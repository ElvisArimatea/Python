'''
---------------------------------------------------------------------------------------------------------------
Neste exemplo é visto o uso do comando "text[::-1]" para inverter a STR, sendo "text" a STR.
---------------------------------------------------------------------------------------------------------------

-> Definição de Palíndromo: frase ou palavra que se pode ler, indiferentemente, da esquerda para direita ou vice-versa.

'''


text = str(input("Digite um texto: \n\n"))

text = text.lower().replace(" ", "") #Trasforma a string "text" em caixa baixa e remove os espaços

palindromo = text[::-1]
print(palindromo)

if palindromo == text:
    print("O texto é um palíndromo!")
else:
    print("O texto não um palíndromo!")




print("\n\n")