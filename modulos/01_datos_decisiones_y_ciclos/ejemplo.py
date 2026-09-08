def contar_inscripciones(edades):
    aceptados = 0
    for edad in edades:
        if 14 <= edad <= 18:
            aceptados += 1
    return aceptados


if __name__ == "__main__":
    print("Aceptados:", contar_inscripciones([13, 14, 16, 18, 19]))
