import random
import sys
sys.path.append('C:\\xampp\\htdocs\\py')
from x.paquete1 import modulo1
modulo1.resultado = modulo1.multiplicar(2,3)
modulo1.m()
print(modulo1.resultado)



caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>/?'


cantidad = random.randint(1, len(caracteres))
cadena = ''.join(random.sample(caracteres, cantidad))

print(cadena)