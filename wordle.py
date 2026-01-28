palabra_secreta = 'auto'
intentos = 6

while intentos > 0:
    palabra = ('ignrese su palabra')

    if palabra == palabra_secreta:
        print('Ganaste!!')
        break
    resultado = ''

    for i in range (len(palabra)):
        if palabra[i] == palabra_secreta[i]:
            resultado += 'correcto'
        elif palabra[i] == palabra_secreta:
            resultado += 'cerca'
        else:
            resultado += 'incorrecto'
    print(resultado)
    intentos -= 1

    if intentos == 0:
        (print 'perdiste la partida')

