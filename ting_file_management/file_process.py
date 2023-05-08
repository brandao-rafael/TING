from ting_file_management.file_management import txt_importer

# import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    file_name = path_file.split("/")[-1]
    for data in instance.get_data():
        if data["nome_do_arquivo"] == file_name:
            print(f"arquivo {file_name} já processado")
            return
    lines_in_file = txt_importer(path_file)
    file_data = {
        "nome_do_arquivo": file_name,
        "qtd_linhas": len(lines_in_file),
        "linhas_no_arquivo": lines_in_file,
    }
    instance.enqueue(file_data)
    print(
        f"'nome_do_arquivo': '{path_file}',"
        + f"'qtd_linhas': {len(lines_in_file)},"
        + f"'linhas_do_arquivo': {lines_in_file}"
    )


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
