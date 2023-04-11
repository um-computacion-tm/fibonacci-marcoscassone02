def fibonacci(digito):
    i=1
    a0=0
    a1=1
    resultado=0
    if digito ==1:
        resultado = 1
    while i < digito:
            resultado = a0+a1
            a0=a1
            a1=resultado
            i+=1
    return resultado
