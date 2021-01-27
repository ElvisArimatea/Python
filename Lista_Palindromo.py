text = str(input("Digite um texto: \n\n"))

text = text.lower().replace(" ", "") #Trasforma a string "text" em caixa baixa e remove os espaços
print(text)

len_text = int(len(text))
auxiliar_len_text = len(text)
count = 0

while count in len_text:
    palindromo[count] = text[auxiliar_len_text]
    auxiliar_len_text -= 1

print(len_text)




print("\n\n")