""" DocString -----
Python é a linguaguem de programação
a tipagem dele é Dinâmica & Forte
str é uma string > Texto.
as Strings são os textos que ficam por dentro da aspas. 
"""
# Aspas simples
print('Feito em aspas simples - Pedro H') # Ambas aspas não tem diferença no resultado final do console.

# Aspas duplas
print("Feito em aspas duplas - Pedro H")

# Escape 
print("Pedro \"Henrique\"")  # Caso queira que as aspas apareça junto com o texto impresso. 

# r
print(r"Pedro \"Henrique\"") # uma Expressão regular, ele vai mostrar a barra invertida + aspas.

# geralmente não se utiliza o Escape + r , pois complica muito os códigos.

# posso utilizar aspas simples e duplas juntas para fazer a mesma função do Escape. 
print(1 , 'Pedro "Henrique"')

#posso inverter também aspas duplas para simples.
print(2, "Pedro 'Henrique'")
