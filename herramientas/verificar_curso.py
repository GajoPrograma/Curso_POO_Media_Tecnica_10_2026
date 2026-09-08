"""Ejecuta ejemplos, contrasta salidas documentadas y valida enlaces locales."""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    errores = []
    ejemplos = sorted(ROOT.glob("modulos/*/ejemplo.py"))
    for ejemplo in ejemplos:
        resultado = subprocess.run([sys.executable, str(ejemplo)], capture_output=True,
                                   text=True, timeout=15)
        if resultado.returncode:
            errores.append(f"{ejemplo.relative_to(ROOT)}: {resultado.stderr}")
            continue
        readme = ejemplo.with_name("README.md").read_text(encoding="utf-8")
        esperado = re.search(r"```text\n(.*?)\n```", readme, re.S).group(1)
        if ejemplo.parent.name.startswith("10_"):
            if "OK" not in resultado.stderr:
                errores.append("El ejemplo de unittest no confirmó OK")
        elif resultado.stdout.strip() != esperado.strip():
            errores.append(f"Salida diferente de la documentada: {ejemplo.relative_to(ROOT)}")
    documentos = list(ROOT.rglob("*.md"))
    for documento in documentos:
        for destino in re.findall(r"\[[^\]]*\]\(([^)]+)\)", documento.read_text(encoding="utf-8")):
            if "://" in destino or destino.startswith("#"):
                continue
            ruta = destino.split("#", 1)[0]
            if ruta and not (documento.parent / ruta).exists():
                errores.append(f"Enlace roto en {documento.relative_to(ROOT)}: {destino}")
    pruebas = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
                             cwd=ROOT, text=True, capture_output=True, timeout=60)
    print(pruebas.stderr)
    if pruebas.returncode:
        errores.append("Fallaron pruebas de proyectos")
    if errores:
        print("\n".join(errores))
        return 1
    print(f"OK: {len(ejemplos)} ejemplos, enlaces de {len(documentos)} documentos y pruebas de proyectos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
