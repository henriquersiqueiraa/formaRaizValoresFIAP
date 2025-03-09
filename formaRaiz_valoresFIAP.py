"""
Inteiro = int
Real = float
Caracter/texto = str
Booleano = bool
\n = quebra de linha
\t = tabulação de texto
"""

valor1 = 10.5
valor2 = 22
valor3 = 1457
valor4 = 30.14

print(valor1)
print(valor2)
print(valor3)
print(valor4)

#formato "format()"
print(f"Valor 1: {valor1:10}".format(valor1).replace(".", ","))
print(f"Valor 2: {valor2:10}".format(valor2).replace(".", ","))
print(f"Valor 3: {valor3:10}".format(valor3).replace(".", ","))
print(f"Valor 4: {valor4:10}".format(valor4).replace(".", ","))