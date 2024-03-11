# aqui eu defini o nome dos arquivos
arquivo_entrada = "texto_em_minusculo.txt"
arquivo_saida = "texto_em_maiusculo.txt"

# abri o arquivo do texto de entrada e li ele
with open(arquivo_entrada, "r") as arquivo:
    conteudo = arquivo.read()

# usei list compreension e map para transformar o texto inteiro em maiúsculo usando upper
conteudo_em_maiusculo = "".join(map(lambda x: x.upper() if x.islower() else x, conteudo))

# por fim eu escrevi o texto no arquivo de saída
with open(arquivo_saida, "w") as arquivo:
    arquivo.write(conteudo_em_maiusculo)

print("arquivo transformado com sucesso")

