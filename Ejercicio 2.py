"""
Caso 1 - Ejercicio 2:

La Lotería del Chocó realiza rifas diarias. Para cobrar premios se aplican
las siguientes reglas tributarias:

- Premios menores a $2.000.000 están exentos.
- Entre $2.000.000 y $10.000.000 se retiene el 10% de impuestos.
- Premios superiores a $10.000.000 tienen 15% de retención más 2% de solidaridad.

Condiciones adicionales:
- Ganadores frecuentes (3 o más premios en 6 meses) pagan un 5% extra.
- Menores de edad reciben el premio a través de tutor y solo el 70% del valor.
- Si el premio es múltiplo de 777, se otorga una bonificación del 10%.

El programa debe mostrar:
- Premio bruto
- Bonificación (si aplica)
- Impuestos aplicados
- Detalle de retenciones
- Monto total a cobrar
- Estado fiscal del ganador
"""


def calcular_premio(premio, es_frecuente, es_menor):

    premio_bruto = premio
    bonificacion = 0

    # Verificar si el premio es múltiplo de 777
    if premio % 777 == 0:
        bonificacion = premio * 0.10
        premio += bonificacion

    impuestos = 0
    detalle = []

    # Aplicar impuestos según el valor del premio
    if premio < 2000000:
        detalle.append("Exento de impuestos")

    elif premio <= 10000000:
        impuestos += premio * 0.10
        detalle.append("10% impuesto")

    else:
        impuestos += premio * 0.15
        impuestos += premio * 0.02
        detalle.append("15% impuesto")
        detalle.append("2% solidaridad")

    # Aplicar recargo por ganador frecuente
    if es_frecuente:
        extra = premio * 0.05
        impuestos += extra
        detalle.append("5% solidaridad frecuente")

    # Calcular valor neto después de impuestos
    neto = premio - impuestos

    # Aplicar reducción por menor de edad
    if es_menor:
        neto *= 0.70
        detalle.append("70% por ser menor de edad")

    # Determinar estado fiscal
    if impuestos == 0:
        estado = "Exento"
    elif impuestos < premio * 0.15:
        estado = "Contribuyente medio"
    else:
        estado = "Alto contribuyente"

    return premio_bruto, bonificacion, impuestos, detalle, neto, estado


# Menú para calcular varios ganadores
while True:

    print("\n--- CÁLCULO DE PREMIO ---")

    # Validación del premio
    try:
        premio = float(input("Ingrese el valor del premio: "))
        if premio < 0:
            print("Error: el premio no puede ser negativo")
            continue
    except:
        print("Error: ingrese un número válido")
        continue

    # Entrada de datos
    frecuente = input("¿Es ganador frecuente? (si/no): ").lower()
    es_frecuente = True if frecuente == "si" else False

    menor = input("¿Es menor de edad? (si/no): ").lower()
    es_menor = True if menor == "si" else False

    # Cálculo
    premio_bruto, bonificacion, impuestos, detalle, neto, estado = calcular_premio(
        premio, es_frecuente, es_menor
    )

    # Resultados
    print("\n--- RESULTADOS ---")
    print("Premio bruto:", premio_bruto)
    print("Bonificación:", bonificacion)
    print("Impuestos:", impuestos)
    print("Detalle de retenciones:", detalle)
    print("Total a cobrar:", neto)
    print("Estado fiscal:", estado)

    # Opción para continuar o salir
    opcion = input("\n¿Desea calcular otro premio? (si/no): ").lower()
    if opcion != "si":
        print("Programa finalizado")
        break