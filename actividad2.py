"""
Inicializo el descuento en 0 porque el programa puede tomarlo como una variable sin definir
"""
descuento = 0

# El programa pide la información al cliente
nombre = input("Ingresá el nombre del cliente: ")
subtotal = float(input("Ingresá el subtotal en dólares (USD): "))

# Evalúa el subtotal para calcular el precio final
if subtotal < 80:
    print(f'Hola {nombre}, el total que debés pagar es de U$S {subtotal}')
elif 80 <= subtotal < 150:
    descuento = 0.1
elif 150 <= subtotal <= 300:
    descuento = 0.15
elif 300 < subtotal < 500:
    descuento = 0.2
total = subtotal - (subtotal * descuento)
print(f'Hola {nombre}, estos son los valores de tu compra:'
      f'\n - Compra sin descuento: U$S {subtotal}'
      f'\n - Compra con descuento del {int(descuento*100)}%: U$S {total}')

"""
Los totales de los siguientes clientes:

Ángel Mario Villa López pagó U$S 364 gracias al descuento del 20%
Rosa Díaz pagó U$S 94.5 gracias al descuento del 10%
Dilan González pagó U$S 212.5 gracias al descuento del 15%
Kelly Daza pagó U$S 344 gracias al descuento del 20%
"""
