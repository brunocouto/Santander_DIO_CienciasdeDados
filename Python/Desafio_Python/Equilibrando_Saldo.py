saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

# TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.


def saldo_conta(saldo_atual, valor_deposito, valor_retirada):
    deposito = saldo_atual + valor_deposito
    saque = deposito - valor_retirada

    return saque


# TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
novo_saldo = saldo_conta(saldo_atual, valor_deposito, valor_retirada)
# print(f'Saldo atualizado em conta: {novo_saldo:.1f}')
# print("Saldo atualizado",{ novo_saldo:.f})
print("Saldo atualizado na conta: {0:.1f}".format(novo_saldo))
