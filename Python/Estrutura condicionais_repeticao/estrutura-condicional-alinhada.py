      

conta_normal = True
conta_universitária = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal >= saque:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Cheque especial de R$" + str(cheque_especial) + " recebido!")
    else:
        print('Saldo insuficiente')
elif conta_universitária:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    else:
        print("saldo insuficiente!")
else:
    print ("Conta inexistente.")
    