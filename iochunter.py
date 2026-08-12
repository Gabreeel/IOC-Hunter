import re
import ipaddress

caminho_arquivo = input("Digite o caminho do arquivo: ")

try:
    with open(caminho_arquivo, 'r', encoding="utf-8") as arquivo_aberto:
        conteudo_arquivo = arquivo_aberto.read()
        caracteres = len(conteudo_arquivo)

    print(f"O arquivo {caminho_arquivo} possui {caracteres} caracteres.\n")

    ipv4_candidatos = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', conteudo_arquivo)

    ipv4_lista = []
    ipv4_falsos_candidatos = []

    for ipv4 in ipv4_candidatos:
        try:
            ipaddress.IPv4Address(ipv4)
            ipv4_lista.append(ipv4)
        except ipaddress.AddressValueError:
            ipv4_falsos_candidatos.append(ipv4)

    quantidade_ipv4 = len(ipv4_lista)
    quantidade_falsos_candidatos = len(ipv4_falsos_candidatos)

    for ipv4 in ipv4_lista:
        print(f"Endereço IPv4 encontrado: {ipv4}")

    print(f"\nQuantidade de endereços IPv4 encontrados: {quantidade_ipv4}")

    for ipv4 in ipv4_falsos_candidatos:
        print(f"\nEndereço IPv4 inválido encontrado: {ipv4}")

    print(f"\nQuantidade de endereços IPv4 inválidos encontrados: {quantidade_falsos_candidatos}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
