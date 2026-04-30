# Programa ElectroChocó

# Entrada de datos
subtotal = float(input("Ingrese el valor de la compra: "))
edad = int(input("Ingrese la edad del cliente: "))
ciudad = input("Ingrese la ciudad del cliente: ").lower()

# Variables de descuentos
descuento_base = 0
descuento_extra = 0
descuento_quibdo = 0

# Descuento escalonado
if 500000 <= subtotal <= 999999:
    descuento_base = subtotal * 0.20
elif subtotal >= 1000000:
    descuento_base = subtotal * 0.25
elif 300000 <= subtotal <= 499999:
    descuento_base = subtotal * 0.15
elif 100000 <= subtotal <= 299999:
    descuento_base = subtotal * 0.10

# Descuento por edad
if edad < 18 or edad > 65:
    descuento_extra = subtotal * 0.05

# Descuento por ciudad (Quibdó)
if ciudad == "quibdo":
    descuento_quibdo = subtotal * 0.03

# Cálculo total de descuentos
ahorro_total = descuento_base + descuento_extra + descuento_quibdo

# Precio final
precio_final = subtotal - ahorro_total

# Salida
print("\n----- FACTURA ELECTROCHOCÓ -----")
print(f"Subtotal: ${subtotal:,.0f}")
print(f"Descuento base: ${descuento_base:,.0f}")
print(f"Descuento por edad: ${descuento_extra:,.0f}")
print(f"Descuento por ciudad: ${descuento_quibdo:,.0f}")
print(f"Ahorro total: ${ahorro_total:,.0f}")
print(f"Precio final: ${precio_final:,.0f}")

# Envío gratis
if subtotal >= 1000000:
    print("Envío: GRATIS")

# Oferta del día
if ahorro_total > 80000:
    print("¡OFERTA DEL DÍA!")