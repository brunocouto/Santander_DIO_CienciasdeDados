nome = "gUIlherME"

print(nome.upper()) # tudo em maiúsculo 
print(nome.lower()) # tudo em minusculo 
print(nome.title()) # primeira letra maiúscula 

texto = "  Ola mundo !    "

print(texto + ".")
print(texto.strip() + ".")# corta espaço em branco 
print(texto.rstrip() + ".") # remove espaço da esquerda e mantém da direita 
print(texto.lstrip() + ".")# remove espaço da esquerda e mantém da direita 


menu = "Python"
print("#####" + menu + "#####")
print(menu.center(14))
print(menu.center(14,"#"))
print("P-y-t-h-o-n")
print("-".join(menu))


