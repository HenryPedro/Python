# \r\n -> CRLF (Windows)
# \n -> LF (Mac)

print (1, 2, 3 ,4, sep='-' , end='#') # sep serve para separar o texto = separador.
print(5, 6, 7, 8, sep='-', end='\r\n #')
print(9, 10 , 11 , 12 , sep='-', end='\n')