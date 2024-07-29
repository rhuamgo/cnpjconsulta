def cnpj(cnpj):
    # Remove caracteres não numéricos
    cnpj = ''.join(filter(str.isdigit, cnpj))
    
    # Verifica se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        return False

    # Lista de multiplicadores dos dígitos
    multiplicadores_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    multiplicadores_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    # Calcula o primeiro dígito verificador
    soma = sum(int(cnpj[i]) * multiplicadores_1[i] for i in range(12))
    primeiro_digito = 11 - (soma % 11)
    if primeiro_digito >= 10:
        primeiro_digito = 0

    # Calcula o segundo dígito verificador
    soma = sum(int(cnpj[i]) * multiplicadores_2[i] for i in range(13))
    segundo_digito = 11 - (soma % 11)
    if segundo_digito >= 10:
        segundo_digito = 0

    # Verifica se os dígitos calculados são iguais aos dígitos do CNPJ fornecido
    return cnpj[-2:] == f'{primeiro_digito}{segundo_digito}'


