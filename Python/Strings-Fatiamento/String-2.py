nome = "Guilherme"
idade =28
profissao = "Programador"
linguagem = "Python"
dados = {"nome": "Guilherme", "idade": 28}

print("Nome: % idade: %d" (nome ,idade))

print("Nome: {} idade: {}".format(nome,idade))

print("Nome: {1} idade: {0}".format(nome,idade))
print("Nome: {1} idade: {0}.nome: {1} {1}".format(idade, nome))

print("nome : {nome} idade: {idade}".format(nome=nome,idade=idade))
print("nome : {nome} idade:{age} {name} {name} {age}".format(age=idade,name=nome))
print("nome:{nome} idade:{idade}".format(**dados))

print (f"nome: {nome} idade:{idade}")
print(f"nome: {nome} idade: {idade} saldo : {saldo:.2f}")
print(f"nome: {nome} idade: {idade} saldo : {saldo:10.2f}")
