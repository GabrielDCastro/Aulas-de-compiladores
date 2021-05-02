# Gabriel de Castro Rangel - RA: 21801612
codigo = str(input("Digite um código\n"))
parada = None
inicio = None
final = None
erro = None
errorsInitBlock = ['/8', '?*', "?8", "?/"]
errorsFimBlock = ["8/", "*?", "8?", "* /"]
errorsInline = ["/?", "?/", "/ /", "??", "\/", "||"]

def olhar_codigo():
    for i in range(len(codigo)):
        if codigo[i] == '/' and codigo[i-1] == '/':
            global parada
            parada = i - 1
            break
        if codigo[i] == '*' and codigo[i-1] == '/':
            global inicio
            inicio = i-1
        if codigo[i] == '/' and codigo[i-1] == '*':
            global final
            final = i

olhar_codigo()
for i in errorsFimBlock:
    if i in codigo:
        erro=i
        codigo=codigo.replace(i, '*/')

for i in errorsInitBlock:
    if i in codigo:
        erro=i
        codigo=codigo.replace(i, '/*')

for i in errorsInline:
    if i in codigo:
        erro=i
        codigo=codigo.replace(i, '//')

if erro:
    print("Código com erro de sintaxe '{}'. Vou corrigi-lo pra você".format(erro))
    olhar_codigo()

if parada:
    for i in range(parada):
        print(codigo[i], end ="")

elif inicio and final:
    for i in range(len(codigo)):
        if (i < inicio or i >final):
            print(codigo[i], end ="")

else:
    print(codigo)
