

datos = ["12", "abc", "45", None, "99"]
for dato in datos:
    try:
        numero = int(dato)
        print(f"Convertido: {numero}")
    except (ValueError, TypeError):
        print(f"Error al convertir: {dato}")

print("esta es una nueva version")