from lib import (
    carregar_sorvetes,
    valores_perigosos,
    exibir_introducao,
    exibir_cena_crime,
    interrogar_suspeito,
    examinar_pista,
    revelar_culpado
)

def main():
    sorvetes = carregar_sorvetes()
    sorvetes_suspeitos = []

    for sorvete in sorvetes:
        if sorvete["nome_sorvete"] != "Choco":
            sorvetes_suspeitos.append(sorvete)

    culpado = None
    for sorvete in sorvetes_suspeitos:
        if sorvete["nome_sorvete"] == "Mentolado":
            culpado = sorvete
            break

    if not culpado:
        print("Erro: O suspeito Mentolado não foi encontrado na lista de sorvetes.")
        return

    exibir_introducao()
    exibir_cena_crime()

    pistas_examinadas = []
    suspeitos_interrogados = []
    consultas_sorvetes = 0

    while True:
        print("\n" + "=" * 50)
        print("O que você deseja fazer?")
        print("1. Examinar uma pista 🔍")
        print("2. Interrogar um suspeito 🗣️")
        print("3. Fazer uma acusação ⚖️")
        print("4. Acessar informações de um sorvete 📄")
        print("5. Acessar tabela de valores perigosos 💣")
        print("6. Sair do jogo ❌")

        opcao = input("> ")

        if opcao == "1":
            if len(pistas_examinadas) >= 3:
                print("\nVocê já examinou o número máximo de pistas!")
                continue

            print("\nEscolha uma pista para examinar:")
            print("1. Pegadas geladas")
            print("2. Recipiente de Lustro derramado")
            print("3. Colher metálica torta")
            print("4. Rachadura no vidro do freezer")

            pista_escolhida = input("> ")

            if pista_escolhida in ["1", "2", "3", "4"]:
                if pista_escolhida not in pistas_examinadas:
                    examinar_pista(pista_escolhida, culpado)
                    pistas_examinadas.append(pista_escolhida)
                else:
                    print("\nVocê já examinou essa pista! Escolha outra.")
            else:
                print("\nOpção inválida. Tente novamente.")

        elif opcao == "2":
            print("\nEscolha um suspeito para interrogar:")
            for i, sorvete in enumerate(sorvetes_suspeitos, 1):
                print(f"{i}. {sorvete['nome_sorvete']} ({sorvete['sabor_sorvete']})")

            escolha = input("> ")

            if escolha.isdigit():
                indice = int(escolha) - 1
                if 0 <= indice < len(sorvetes_suspeitos):
                    suspeito = sorvetes_suspeitos[indice]
                    if suspeito["nome_sorvete"] not in suspeitos_interrogados:
                        interrogar_suspeito(suspeito, culpado)
                        suspeitos_interrogados.append(suspeito["nome_sorvete"])
                    else:
                        print("\nVocê já interrogou esse suspeito! Escolha outro.")
                else:
                    print("\nNúmero inválido. Escolha um dos suspeitos listados.")
            else:
                print("\nEntrada inválida. Digite um número.")

        elif opcao == "3":
            print("\nQuem você acha que é o culpado?")
            for i, sorvete in enumerate(sorvetes_suspeitos, 1):
                print(f"{i}. {sorvete['nome_sorvete']} ({sorvete['sabor_sorvete']})")

            escolha = input("> ")

            if escolha.isdigit():
                indice = int(escolha) - 1
                if 0 <= indice < len(sorvetes_suspeitos):
                    acusado = sorvetes_suspeitos[indice]
                    revelar_culpado(acusado, culpado)
                    acusacoes_restantes -= 1
                    if acusado == culpado:
                        break
                else:
                    print("\nNúmero inválido. Escolha um dos suspeitos listados.")
            else:
                print("\nEntrada inválida. Digite um número.")

        elif opcao == "4":
            if consultas_sorvetes < 3:
                print("\nEscolha um sorvete para acessar as informações:")
                for i, sorvete in enumerate(sorvetes_suspeitos, 1):
                    print(f"{i}. {sorvete['nome_sorvete']} ({sorvete['sabor_sorvete']})")

                escolha = input("> ")

                if escolha.isdigit():
                    indice = int(escolha) - 1
                    if 0 <= indice < len(sorvetes_suspeitos):
                        sorvete = sorvetes_suspeitos[indice]
                        print("\nInformações do sorvete:")
                        print(f"Nome: {sorvete['nome_sorvete']}")
                        print(f"Aparência: {sorvete['aparencia']}")
                        print(f"Consciência: {sorvete['consciencia']}")
                        print(f"Quantidade de Lustro: {sorvete['quantidade_lustro']}")
                        print(f"Personalidade: {sorvete['personalidade']}")
                        print(f"Nível de Derretimento: {sorvete['nivel_derretimento']}")
                        print(f"Freezer: {sorvete['freezer']}")
                        consultas_sorvetes += 1
                    else:
                        print("\nNúmero inválido. Escolha um dos suspeitos listados.")
                else:
                    print("\nEntrada inválida. Digite um número.")
            else:
                print("\nVocê já acessou as informações dos sorvetes 3 vezes. Não pode acessar mais.")

        elif opcao == "5":
            print("\n 🚨 ALERTA! Os seguintes valores ultrapassam os limites seguros. Proceda com cautela... 🚨")
            valores_perigosos()

        elif opcao == "6":
            print("\nObrigado por jogar Crimelatto: O Enigma dos Sabores! 🍦🔎")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()