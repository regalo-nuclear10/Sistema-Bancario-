from time import sleep
import datetime
def linha():
	print('=+' * 15)
saldo = 0
LIMITE_POR_SAQUE = 500.00
TransacoesDiarias = 10
extrato = ''
dia_hoje = datetime.date.today().strftime("%d/%m/%Y")
linha()
print(f'{"Banco Regalo":^30}')
while True:
	linha()
	print('''[1] Depósito
[2] Saque
[3] Extrato
[4] Sair''')
	linha()
	sucesso = False
	opção = str(input('Sua opção: ')) 
	
	match opção:
		case '1' |  '2':
			if TransacoesDiarias <= 0:
				print(f'As suas transações para o dia {dia_hoje} terminaram! Volte amanhã.')
				sleep(1.2)
			else:
				if opção == '1':
					linha()
					print(f'{"Depósito":^30}')
					linha()
					depósito = float(input('Valor a depositar: '))
					if depósito < 0.01:
						print('O valor depositado deve ser acima de R$0.00')
						sleep(1)
					elif depósito > 5000:
						print('Não se pode depositar mais de R$5000.00')
					else:
						saldo += depósito
						print(f'Depósito de R${depósito:.2f} feito com sucesso.\nSeu saldo atual é de R${saldo:.2f}')
						sucesso = True
						data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M %a")
						extrato += f'Depósito: R${depósito:.2f} data: {data}\n'
						sleep(1)
					
				elif opção == '2':
					if saldo == 0:
						print('Sua conta não possui saldo')
					else:
						linha()
						print(f'{"Saque":^30}')
						linha()
						saque = float(input('Valor a sacar: '))
						if saque > LIMITE_POR_SAQUE :
								print(f'O limite de  saque é de {LIMITE_POR_SAQUE:.2f}')
						elif saque <= 0 or saque > saldo:
							print('Não é possível sacar esse valor')
						else:
							saldo -= saque
							print(f'Saque feito com sucesso\n Seu saldo atual é de R${saldo:.2f}')
							sucesso = True
							data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M %a")
							extrato += f'Saque: {saque:.2f} data: {data}\n'
			if sucesso:
				TransacoesDiarias -= 1
				print(f'Restam {TransacoesDiarias} transações para o dia de hoje: {dia_hoje}')	
		case '3':
			linha()
			print(f'{"Extrato":^30}')
			linha()
			print(f'Não foram feitos movimentos' if not extrato else extrato)
			print(f'Saldo atual: {saldo:.2f}')
			print(f'Restam {TransacoesDiarias} transacões pra hoje: {dia_hoje}')
			sleep(1)
		case '4':
			print('Saindo...')
			break
		case _:
			print('Opção inválida.Tente de novo.')
 