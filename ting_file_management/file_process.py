from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    file_name = path_file.split("/")[-1]
    for data in instance.get_data():
        if data["nome_do_arquivo"] == path_file:
            print(f"arquivo {file_name} já processado")
            return
    lines_in_file = txt_importer(path_file)
    file_data = {
        "nome_do_arquivo": path_file,
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
    deleted_file = instance.dequeue()
    if deleted_file is None:
        print("Não há elementos")
        return
    print(f"Arquivo {deleted_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
