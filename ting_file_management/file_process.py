from ting_file_management.file_management import txt_importer

# import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    file_name = path_file.split("/")[-1]
    line_quantity = len(instance)
    for i, data in enumerate(instance.get_data()):
        if data[i] == file_name:
            line_quantity -= 1
    lines_in_file = txt_importer(path_file)
    file_data = {
        "nome_do_arquivo": file_name,
        "qtd_linhas": line_quantity,
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
