palavra = str(input("Digite a palavra a ser adivinhada: "))

print('_' * len(palavra))

letra = str(input("Digite uma letra: "))
teste = palavra

while letra != '0':
    teste = teste.replace(letra, '_')
    print(teste)
    letra = str(input("Digite uma letra: "))
    


for i in range(len(palavra)):
    if teste[i] != '_':
        forca = forca + ' ' + teste[i]



