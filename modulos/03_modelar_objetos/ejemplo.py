def prestar(libro):
    if not libro["disponible"]:
        return False
    libro["disponible"] = False
    return True


if __name__ == "__main__":
    libro = {"codigo": "L1", "titulo": "Robótica", "disponible": True}
    print("Primer préstamo:", prestar(libro))
    print("Segundo préstamo:", prestar(libro))
