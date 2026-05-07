def calcular_asistencia():
    presentes = 0
    total = 0

    print("Ingrese la asistencia (P = Presente, A = Ausente, TOTAL para terminar):")

    while True:
        dato = input().upper()

        if dato == "TOTAL":
            break
        elif dato == "P":
            presentes += 1
            total += 1
        elif dato == "A":
            total += 1
        else:
            print("Entrada inválida. Use P, A o TOTAL.")

    return presentes, total


def porcentaje_asistencia(presentes, total):
    if total == 0:
        return 0
    return (presentes / total) * 100


# Programa principal
nombre = input("Ingrese el nombre del estudiante: ")

presentes, total = calcular_asistencia()
porcentaje = porcentaje_asistencia(presentes, total)

print(f"\n{nombre}: {porcentaje:.0f}% ", end="")

if porcentaje < 70:
    print("RECUPERACIÓN")
else:
    print("OK")