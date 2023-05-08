def exists_word(word, instance):
    """Aqui irá sua implementaçã"""
    result = []
    print(instance.get_data())
    for data in instance.get_data():
        rows = []
        for i, line in enumerate(data["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                rows.append({"linha": i + 1})
        if rows:
            result.append(
                {
                    "palavra": word,
                    "arquivo": data["nome_do_arquivo"],
                    "ocorrencias": rows,
                }
            )
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    result = []
    print(instance.get_data())
    for data in instance.get_data():
        rows = []
        for i, line in enumerate(data["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                rows.append({"linha": i + 1, "conteudo": line})
        if rows:
            result.append(
                {
                    "palavra": word,
                    "arquivo": data["nome_do_arquivo"],
                    "ocorrencias": rows,
                }
            )
    return result
