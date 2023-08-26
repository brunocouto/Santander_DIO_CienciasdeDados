texto   =   input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if(letra.upper() not in VOGAIS):
        print (letra, end="")
        
print()

#tabuada
for numero in range(0,51,5):
    print(numero)
    print(numero,end="")