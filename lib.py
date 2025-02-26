import csv

def carregar_sorvetes(caminho_csv):
    with open(caminho_csv, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo, delimiter=';')
        next(leitor_csv)

        for linha in leitor_csv:
            sabor = linha[0]
            nome = linha[1]
            aparencia = linha[2]
            consciencia = linha[3]
            quantidade_lustro = linha[4]
            personalidade = linha[5]
            personalidade_oculta = linha[6]
            nivel_derretimento = linha[7]
            freezer = linha[8]

            print(f"Sabor: {sabor}")
            print(f"Nome: {nome}")
            print(f"Aparência: {aparencia}")
            print(f"Consciência: {consciencia}")
            print(f"Quantidade de Lustro: {quantidade_lustro}")
            print(f"Personalidade: {personalidade}")
            print(f"Personalidade Oculta: {personalidade_oculta}")
            print(f"Nível de Derretimento: {nivel_derretimento}")
            print(f"Freezer: {freezer}")
            print("-" * 30)

if __name__ == "__main__":
    caminho_csv = "sorvetes.csv"
    carregar_sorvetes(caminho_csv)