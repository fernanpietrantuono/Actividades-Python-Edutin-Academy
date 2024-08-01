print("Bienvenido al conversor de divisas 💸")


def conversor(moneda_actual, monto, moneda_a_cambiar):
    if moneda_actual == 1:
        def dolar_to():
            if moneda_a_cambiar == "1":
                print(f'USD {monto} son COP {monto * 3750}')
            elif moneda_a_cambiar == "2":
                print(f'USD {monto} son ¥ {monto * 6.37}')
            elif moneda_a_cambiar == "3":
                print(f'USD {monto} son £ {monto * 0.76}')
            else:
                print("Lo siento, no tenemos esa moneda que nos pediste 🙁")

        dolar_to()
    elif moneda_actual == 2:
        def euro_to():
            if moneda_a_cambiar == "1":
                print(f'€ {monto} son COP {monto * 4000}')
            elif moneda_a_cambiar == "2":
                print(f'€ {monto} son ¥ {monto * 6.93}')
            elif moneda_a_cambiar == "3":
                print(f'€ {monto} son £ {monto * 0.83}')
            else:
                print("Lo siento, no tenemos esa moneda que nos pediste 🙁")

        euro_to()
    else:
        print("Lo siento, no tenemos esa moneda que nos pediste 🙁")


moneda_vigente = int(input("Ingresá la moneda actual: \n"
                           "1. Dólar Estadounidense (USD) \n"
                           "2. Euro (EUR) \n"))
importe = float(input("Ingresá el valor: "))
moneda_nueva = input("Elegí una moneda nueva: \n"
                     "1. Pesos Colombianos (COP) \n"
                     "2. Yuanes Renminbi (CNY) \n"
                     "3. Libras Esterlinas (GBP) \n")

conversor(moneda_vigente, importe, moneda_nueva)

"""
Las conversiones recientes:

U$S 50 → COP 187500
€ 30 → ¥ 207.89
€ 15 → £ 12.45
"""
