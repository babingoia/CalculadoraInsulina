import Classes
from Banco_de_dados import comidas

# Inicializando variaveis globais
loop = 0
calorias_totais, insulina_total = 0, 0
tabela_substituicao_caracteres = str.maketrans({
    "á": "a", "Á": "A",
    "ã": "a", "Ã": "A",
    "à": "a", "À": "A",
    "â": "a", "Â": "A",
    "é": "e", "É": "E",
    "è": "e", "È": "E",
    "ê": "e", "Ê": "E",
    "í": "i", "Í": "I",
    "ì": "i", "Ì": "I",
    "î": "i", "Î": "I",
    "ó": "o", "Ó": "O",
    "ò": "o", "Ò": "O",
    "õ": "o", "Õ": "O",
    "ô": "o", "Ô": "O",
    "ú": "u", "Ú": "U",
    "ù": "u", "Ù": "U",
    "û": "u", "Û": "U"
})


def pesquisa(escolha):

    pesquisas_encontradas = []
    pesquisa_tratada = tratar_pesquisa(escolha)

    for nome_comida, comida in comidas.items():
        if nome_comida == pesquisa_tratada:
            return comida

        elif nome_comida.endswith(pesquisa_tratada) or nome_comida.startswith(pesquisa_tratada) or \
                pesquisa_tratada in nome_comida:
            pesquisas_encontradas.append(nome_comida)

    if pesquisas_encontradas:
        return pesquisas_encontradas

    raise ValueError("Não pude encontrar sua pesquisa!")


def tratar_pesquisa(escolha):
    global tabela_substituicao_caracteres
    tratando_pesquisa = escolha.strip()
    tratando_pesquisa = tratando_pesquisa.translate(tabela_substituicao_caracteres)
    tratando_pesquisa = tratando_pesquisa.lower()

    return tratando_pesquisa


def escolher_comida():
    while True:
        try:
            comida_pesquisada = pesquisa(input("Insira a comida a ser calculada:\n"))

            if isinstance(comida_pesquisada, Classes.ComidaGenerica):
                return comida_pesquisada

            print(f"Esses foram os resultados encontrados: {comida_pesquisada}\n"
                  f"digite denovo por favor:")

        except ValueError as error:
            print(error)
            continuar = input("Deseja continuar e tentar novamente(s/n)?")
            if continuar == "n":
                quit()


def calcular_tudo():
    global insulina_total, calorias_totais, meta_insulina, quantidade_comida

    insulina_total = comida_escolhida.calcular_insulina(meta_insulina, quantidade_comida) + insulina_total
    calorias_totais = comida_escolhida.calcular_calorias(quantidade_comida) + calorias_totais

    print(f"A quantidade de calorias dessa refeição foi de: {calorias_totais} Kcal\n"
          f"Insulina: {insulina_total} unidades\n")


meta_insulina = int(input(f"Bem vindo a calculadora de calorias e insulina!\n "
                          f"Primeiro digite sua meta de carboidratos por unidade.\n"))

while True:
    # Pega as infos do usuário
    print("Comidas Disponiveis:\n")
    for nome in comidas:
        print(f"{nome}")
    print("\n")

    comida_escolhida = escolher_comida()
    quantidade_comida = int(input("Qual a quantidade dela em gramas?\n"))
    calcular_tudo()

    terminar_loop = input("Deseja continuar? (s/n)\n")

    if terminar_loop != 's':
        break
# Colocar um sistema para perguntar se deseja somar a quantidade anterior com a próxima

# Colocar um terceiro sistema que define a meta do dextro e descontar do atual

# Achar um jeito melhor de guardar as infos do banco de dados.

# Botar funcao que registra no banco de dados o dextro e a insulina
