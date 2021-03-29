from random import randrange

vidas = 5
win = 1

lista_palavra = open("Palavras_forca.txt", "r")     #Abre o arquivo de palavras e o colocada na variavel "lista_palavra"
lista_palavra = list(lista_palavra)                 #Divide as palavras em lista
n_palavra = randrange(0, len(lista_palavra))        #Gera um número aleatório para escolher a palavra
#print(n_palavra)

palavra = lista_palavra[n_palavra].upper().strip()  #Tira espaços e coloca as letras em maiusculas
#print(palavra)

forca = '_' * len(palavra)
forca = list(forca) #Divide cada caracter de "forca" na string, como se fosse uma lista, com posição
print(' '.join(forca)) #Une todas as strings colocando ' ' entre elas (' '.join(forca))

resultado = '_'
mascara = list(palavra)
letra = ''


while resultado.count('_') > 0 and letra != '0':
    letra = str(input("Digite uma letra: ")).upper()
    
    if mascara.count(letra) > 0:
        aux = palavra.find(letra)
        
        for i in range(0, palavra.count(letra)):            
            forca [aux] = letra            
            aux = palavra.find(letra, aux+1) #Procura a proxima ocorrencia da letra em aux+1 (aux+1 porque se não ele acha a mesma letra novamente)
    else:
        vidas -= 1
        #print(vidas)
        if vidas <= 0:
            print("Você perdeu!")
            win = 0 #auxiliar para não entrar no if do ganhar
            break
        elif vidas > 0:
            #print("Você acaba de perder uma vida!")
            print("ERROU! Vidas restantes: ", vidas)

    resultado = ' '.join(forca)
    print(resultado)

if win != 0:
    print("Parabéns! Você adivinhou a palavra:", palavra)
    

