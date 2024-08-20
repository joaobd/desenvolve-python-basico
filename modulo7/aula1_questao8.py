def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = cpf.replace('.', '').replace('-', '')

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = (soma * 10 % 11) % 10

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = (soma * 10 % 11) % 10

    # Verifica se os dígitos verificadores estão corretos
    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"

cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
if validar_cpf(cpf):
    print("Válido")
else:
    print("Inválido")