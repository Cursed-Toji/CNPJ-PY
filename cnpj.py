def formatar_cnpj(cnpj):
    # Remove caracteres não numéricos
    cnpj = ''.join(filter(str.isdigit, cnpj))
    
    # Verifica se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        return "CNPJ inválido"

    # Formata o CNPJ
    cnpj_formatado = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
    
    return cnpj_formatado

def main():
    while True:
        cnpj = input("Digite o CNPJ: ")
        if cnpj.lower() in ['exit', 'sair', 'quit']:
            break
        print(formatar_cnpj(cnpj))

if __name__ == "__main__":
    main()
