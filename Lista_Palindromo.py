text = str(input("Digite um texto: \n\n"))

text = text.lower().replace(" ", "") #Trasforma a string "text" em caixa baixa e remove os espaços

palindromo = text[::-1]
print(palindromo)

if palindromo == text:
    print("O texto é um palíndromo!")
else:
    print("O texto não um palíndromo!")




print("\n\n")