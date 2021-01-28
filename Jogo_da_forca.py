palavra = str(input("Digite a palavra a ser adivinhada: ")).upper()
forca = '_' * len(palavra)
forca = list(forca)
print(' '.join(forca))

resultado = '_'
mascara = list(palavra)
letra = ''

while resultado.count('_') > 0 and letra != '0':
    letra = str(input("Digite uma letra: ")).upper()
    
    if mascara.count(letra) > 0:
        aux = palavra.find(letra)
        
        for i in range(0, palavra.count(letra)):            
            forca [aux] = letra            
            aux = palavra.find(letra, aux+1)
    
    resultado = ' '.join(forca)
    print(resultado)

print("Parabéns! Você adivinhou a palavra:", palavra)
    

