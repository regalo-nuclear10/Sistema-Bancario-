from time import sleep
AGENCIA = '0001'
saldo = 0
LIMITE_POR_SAQUE = 500.00
SaquesDiarios = 3
extrato = ''
usuarios = []
contas = []
numero_conta = 0

def linha():
	print('=+' * 15)


def menu():
	linha()
	print('''[1] Depósito
[2] Saque
[3] Extrato
[4] Criar conta
[5] Criar usuário
[6] Listar contas
[7] Sair''')
	linha()
	opcao = str(input('Sua opção: ')) 
	return opcao
	
	
def depositar(deposito,extrato_antigo,valor_saldo):
	if deposito < 0.01:
		print('O valor depositado deve ser acima de R$0.00')
		sleep(1)
	else:
		valor_saldo += deposito
		print(f'Depósito de R${deposito:.2f} feito com sucesso.\nSeu saldo atual é de R${valor_saldo:.2f}')
		extrato_antigo += f'{"Depósito:":<15}R${deposito:.2f}\n'
		sleep(1)
	return valor_saldo, extrato_antigo
	
	
def sacar(*,valor_saldo, valor, extrato_antigo):
	
	global LIMITE_POR_SAQUE, SaquesDiarios
	
	if valor > LIMITE_POR_SAQUE :
		print(f'O limite de  saque é de {LIMITE_POR_SAQUE:.2f}')
	elif valor <= 0:
		print('Não é possível sacar esse valor')
	elif valor > valor_saldo:
		print('Não há dinheiro suficiente na conta!')
	else:
		valor_saldo -= valor
		print(f'Saque feito com sucesso. Saldo atual: {valor_saldo:.2f}')
		SaquesDiarios -= 1
		extrato_antigo += f'{"Saque:":<15}R${valor:.2f}\n'
	return valor_saldo, extrato_antigo
	

def mostrar_extrato(valor_saldo,/,*,extrato_antigo):
	linha()
	print(f'{"Extrato":^30}')
	linha()
	print(f'Não foram feitos movimentos' if not extrato else extrato)
	print(f'Saldo atual: {saldo:.2f}')
	

def criar_usuario(usuarios):
	cpf = input('informe seu cpf(somente números): ')
	usuario = filtrar_usuario(cpf, usuarios)
	if usuario:
		print('Já existe um usuário com esse cpf')
	else:
		nome = input('Digite seu nome completo: ')
		nasc = input('Sua data de nascimento(dd-mm-aaaa): ')
		endereço = input('Informe seu endereço( logradouro, nro-bairro-cidade/sigla): ')
		
		usuarios.append({'nome': nome, 'data de nascimento': nasc, 'CPF': cpf, 'endereço': endereço})
		print('Usuário criado com sucesso')
		

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print('Não existe esse CPF')
		


def filtrar_usuario(Cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == Cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_contas(contas):
    for conta in contas:
        print(f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """)


linha()
print(f'{"Banco Regalo":^30}')
while True:
	opcao = menu()
	match opcao:
		case '1':
			linha()
			print(f'{"Depósito":^30}')
			linha()
			valor_deposito = float(input('Valor a depositar: R$ '))
			saldo, extrato = depositar(valor_deposito, extrato, saldo)
			
				
		case '2':
			if saldo == 0:
				print('Sua conta não possui saldo')
				sleep(2)
			elif SaquesDiarios == 0:
				print('Terminaram seus saques diários')
				sleep(2)
			else:
				linha()
				print(f'{"Saque":^30}')
				linha()
				saque = float(input('Valor a sacar: R$'))
				saldo, extrato = sacar(valor_saldo=saldo,valor=saque, extrato_antigo=extrato)
				
		case '3':
			mostrar_extrato(saldo, extrato_antigo=extrato)
			
		case '4':
			numero_conta += 1
			conta = criar_conta(AGENCIA, numero_conta, usuarios)
			if conta:
				contas.append(conta)
				
		case '5':
			criar_usuario(usuarios)
			
		case '6':
			listar_contas(contas)
			
		case '7':
			print('Saindo...')
			break
		case _:
			print('Opção inválida.Tente de novo.')
 