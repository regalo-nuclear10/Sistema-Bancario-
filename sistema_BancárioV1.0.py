from time import sleep
def linha():
	print('=+' * 15)
saldo = 0
LIMITE_POR_SAQUE = 500.00
SaquesDiários = 3
extrato = ''
	
linha()
print(f'{"Banco Regalo":^30}')
while True:
	linha()
	print('''[1] Depósito
[2] Saque
[3] Extrato
[4] Sair''')
	linha()
	opção = str(input('Sua opção: ')) 
	
	match opção:
		case '1':
			linha()
			print(f'{"Depósito":^30}')
			linha()
			depósito = float(input('Valor a depositar: '))
			if depósito < 0.01:
				print('O valor depositado deve ser acima de R$0.00')
				sleep(1)
			else:
				saldo += depósito
				print(f'Depósito de R${depósito:.2f} feito com sucesso.\nSeu saldo atual é de R${saldo:.2f}')
				extrato += f'Depósito: R${depósito:.2f}'
				sleep(1)
		case '2':
			if saldo == 0:
				print('Sua conta não possui saldo')
				sleep(2)
			elif SaquesDiários == 0:
				print('Terminaram seus saques diários')
				sleep(2)
			else:
				linha()
				print(f'{"Saque":^30}')
				linha()
				saque = float(input('Valor a sacar: '))
				if saque > LIMITE_POR_SAQUE :
						print(f'O limite de  saque é de {LIMITE_POR_SAQUE:.2f}')
				elif saque <= 0:
					print('Não é possível sacar esse valor')
				else:
					saldo -= saque
					print('Saque feito com sucesso')
					SaquesDiários -= 1
					extrato += f'Saque: {saque:.2f}'
		case '3':
			linha()
			print(f'{"Extrato":^30}')
			linha()
			print(f'Não foram feitos movimentos' if not extrato else extrato)
		case '4':
			print('Saindo...')
			break
		case _:
			print('Opção inválida.Tente de novo.')
 