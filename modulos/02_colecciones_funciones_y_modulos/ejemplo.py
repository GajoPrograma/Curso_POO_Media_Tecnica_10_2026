def total_unidades(inventario):
    total = 0
    for cantidad in inventario.values():
        total += cantidad
    return total


if __name__ == "__main__":
    materiales = {"led": 4, "cable": 3}
    print("Unidades:", total_unidades(materiales))
    print("Inventario vacío:", total_unidades({}))
