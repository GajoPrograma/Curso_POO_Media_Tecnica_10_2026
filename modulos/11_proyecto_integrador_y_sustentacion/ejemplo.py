def listo_para_entregar(requisitos):
    return bool(requisitos) and all(r["verificado"] for r in requisitos)


if __name__ == "__main__":
    requisitos = [
        {"id": "REQ-01", "verificado": True},
        {"id": "REQ-02", "verificado": False},
    ]
    print("Listo:", listo_para_entregar(requisitos))
    print("Sin requisitos:", listo_para_entregar([]))
