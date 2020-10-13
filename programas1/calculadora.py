arr = [0]*2
operador = ''
resultado = 0

for i in range(0, 2, 1):
    arr[i] = float(input("Dame un numero: " + str(i) + ": "))
    print(arr[i])

operador = input("Operador: ")

if operador == '+':
    resultado = arr[0] + arr[1]
elif operador == '-':
    resultado = arr[0] - arr[1]
elif operador == '*':
    resultado = arr[0] * arr[1]
elif operador == '/':
    resultado = arr[0] / arr[1]
else:
    exit(-1)

print(resultado)
exit(0)

