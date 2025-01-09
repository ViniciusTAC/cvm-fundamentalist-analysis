def formatar_cnpj_colocar_simbolos(cnpj: str) -> str:
    """
    Adiciona os símbolos padrão a um CNPJ, formatando-o para o formato: 00.000.000/0000-00.

    Args:
        cnpj (str): Uma string contendo o CNPJ apenas com números, sem símbolos.

    Returns:
        str: O CNPJ formatado com os símbolos padrão.
    """
    # Divide a string do CNPJ nas posições adequadas e insere os símbolos de formatação.
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"


def formatar_cnpj_remover_simbolos(cnpj: str) -> str:
    """
    Remove os símbolos de um CNPJ formatado, deixando apenas os números.

    Args:
        cnpj (str): Uma string contendo o CNPJ formatado (ex.: 00.000.000/0000-00).

    Returns:
        str: O CNPJ com todos os símbolos removidos, apenas números.
    """
    # Remove os caracteres ".", "/", e "-" de um CNPJ formatado.
    return cnpj.replace(".", "").replace("/", "").replace("-", "")


# Exemplo de formatação

# Formata um CNPJ sem símbolos para o formato padrão.
cnpjSemSimbolo = formatar_cnpj_colocar_simbolos("92839181000162")

# Remove os símbolos de um CNPJ formatado.
cnpjComSimbolo = formatar_cnpj_remover_simbolos("53.916.539/0001-51")

# Exibe os resultados formatados no console.
print(cnpjSemSimbolo)  # Saída esperada: 92.839.181/0001-62
print(cnpjComSimbolo)  # Saída esperada: 53916539000151
