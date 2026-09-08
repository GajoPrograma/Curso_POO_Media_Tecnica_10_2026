def equipos_necesarios(estudiantes):
    if type(estudiantes) is not int or estudiantes < 0:
        raise ValueError("Se necesita una cantidad entera no negativa")
    parejas = estudiantes // 2
    sin_pareja = estudiantes % 2
    return parejas + sin_pareja


if __name__ == "__main__":
    for cantidad in [0, 1, 2, 5, 40]:
        print(cantidad, "estudiantes ->", equipos_necesarios(cantidad), "equipos")
