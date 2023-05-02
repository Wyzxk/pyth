def sumar_dos():
    while True:
            a = input("primer número")
            b = input("segundo número")
            try:
                resultado = int(a) + int(b)
                
            except:
                   print("Error")
            else: break
    return resultado

print(sumar_dos())