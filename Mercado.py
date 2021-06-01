# mercado-only
Mercado de  compras em Python. 

import os

## Tabela de cores ANSI (Python) ##
global C,R,O,W,L,E,Y,a,l,e,i,s,t,ë,r,XV,XXI

# fonte #
C='\033[1;30m'     # Preto 
R='\033[1;31m'     # Vermelho 
O='\033[1;32m'     # Verde 
W='\033[1;33m'    # Amarelo 
L='\033[1;34m'     # Azul 
E='\033[1;35m'     # Rosa
Y='\033[1;36m'     # Ciano

##
XV='\033[1;37m'     # Branco
XXI='\033[0;0m'      # Remover
##

# fundo #
a='\033[1;40m'     # Preto
l='\033[1;41m'      # Vermelho
e='\033[1;42m'     # Verde
i='\033[1;43m'      # Amarelo
s='\033[1;44m'     # Azul
t='\033[1;45m'      # Rosa
ë='\033[1;46m'     # Ciano
r='\033[;7m'          # Inverte 

######
print(f'''
{C}●▬▬▬▬๑▬▬▬▬๑▬▬▬▬●
{XV}     Mercado
{C}   ●▬▬▬▬๑▬▬▬▬๑▬▬▬▬●
{XV}         Do
{C}   ●▬▬▬▬๑▬▬▬▬๑▬▬▬▬●
{XV}   Zeus Xereca
{C}●▬▬▬▬๑▬▬▬▬๑▬▬▬▬●
''')
opção = 0
while opção != 6:
	print(f'''{R}【{W}1{R}】{Y}Arroz {L} R$23.00
{R}【{W}2{R}】{Y}Feijão{L} R$9.89 {W}(promoção)
{R}【{W}3{R}】{Y}Macarrão {L}R$3.49 {W}(oferta)
{R}【{W}4{R}】{Y}Pão de forma {L}R$5.00
{R}【{W}5{R}】{Y}Manteiga {L}R$4.50
{R}【{W}6{R}】{Y}Sair ''')

	opção = float(input(f'\n{r}{XV}Digite o numero do item que você deseja:{XXI}{W} '))
	if opção == 1:
		print(f'{W}O arroz custa {Y}R$23,00{W}, você me deu {Y}R$50,00{W}. Aqui esta seu troco{Y}(R$27,00){W}! Obrigado, volte sempre!\n')
	elif opção == 2:
		print(f'{W}O feijão custa {Y}R$9,89{W}, você me deu {Y}R$20,00{W}. Aqui esta seu troco{Y}(R$10,11){W}! Obrigado, volte sempre!\n')
	elif opção == 3:
		print(f'{W}O macarrão custa {Y}R$3,49{W}, você me deu {Y}R$17,00{W}. Aqui esta seu troco{Y}(R$13,51){W}! Obrigado, volte sempre!\n')
	elif opção == 4:
		print(f'{W}O pão de forma custa {Y}R$5,00{W}, você me deu {Y}R$6,00{W}. Aqui esta seu troco{Y}(R$1,00){W}! Obrigado, volte sempre!\n')
	elif opção == 5:
		print(f'{W}A manteiga  custa {Y}R$4,50{W}, você me deu {Y}R$5,60{W}. Aqui esta seu troco{Y}(R$1.10){W}! Obrigado, volte sempre!\n')
	else:
		os.system('clear')
		exit()
