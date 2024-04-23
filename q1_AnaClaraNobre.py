import uuid

Conta = lambda nome, senha, saldo: {'id': str(uuid.uuid4()), 'nome': nome, 'senha': senha, 'saldo': saldo}

pessoas = [
    {'nome': 'Bob', 'saldo': 2000},
    {'nome': 'Carol', 'saldo': 1000},
    {'nome': 'David', 'saldo': 500}
]

Banco = lambda: {'contas': []}

criar_conta = lambda banco, nome, senha, saldo: (
    lambda conta: banco['contas'].append(conta)
)(Conta(nome, senha, saldo))

logar_conta = lambda banco, nome, senha: (
    lambda conta: conta if conta else None
)(next((conta for conta in banco['contas'] if conta['nome'] == nome and conta['senha'] == senha), None))

sacar = lambda conta, valor: (
    print("OPÇÃO DE SAQUE\nTransação de saque de $%.2f realizada com sucesso!\n--------RECIBO DE SAQUE-----------\nID da Conta: %s\nNome do Usuário: %s\nQuantidade Sacada: $%.2f\nSaldo Restante: $%.2f\n----------------------------------\n" % (
        valor, conta['id'], conta['nome'], valor, conta['saldo'] - valor
    )) if valor <= conta['saldo'] else print("OPÇÃO DE SAQUE\nSaldo insuficiente. Seu saldo disponível é de $%.2f." % conta['saldo']), conta['saldo'] - valor if valor <= conta['saldo'] else conta['saldo']
)

credito = lambda conta, valor: (
    print("OPÇÃO DE CRÉDITO\n------------ESTADO ATUAL DA CONTA------------\nID da Conta:", conta['id'], "\nNome do Usuário:", conta['nome'], "\nSaldo Disponível: $%.2f\n-----------------------------------" % conta['saldo']),
    print("Banco aprovou seu pedido!\nTransação de crédito de $%.2f realizada com sucesso!" % (valor)), conta['saldo'] + valor
) if valor > 0 else (print("Valor de crédito inválido."), conta['saldo'])

transferencia = lambda origem, destino_nome, valor, pessoas, contas: (
    (print(f"OPÇÃO DE TRANSFERÊNCIA\nUSUÁRIA {destino_nome} ENCONTRADA!\nTransferência de {valor} de {origem['nome']} para {destino_nome} realizada com sucesso.") if any(destino_nome == pessoa['nome'] for pessoa in pessoas) else print("OPÇÃO DE TRANSFERÊNCIA\n Usuário para transferência não encontrado.")) if origem and origem['saldo'] >= valor else (print("OPÇÃO DE TRANSFERÊNCIA\nSaldo insuficiente para realizar a transferência."), None)
)
