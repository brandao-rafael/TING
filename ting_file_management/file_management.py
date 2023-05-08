import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido")
    try:
        with open(path_file, mode="r", encoding="utf-8") as file:
            return list(file.read().split("\n"))
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return None
