nome = 'Pedro Henrique'
altura = 1.65
peso = 55
imc = peso / (altura * altura) # Ou pode usar a precedencia, altura ** 2 

"f-strings"

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f' pesa {peso} Kg e seu imc é {imc:.2f}'
print(linha_1 , linha_2);
