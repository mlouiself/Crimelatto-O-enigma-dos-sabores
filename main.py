import time
import random
from lib import carregar_sorvetes, investigar_cena_crime, mostrar_pistas, interrogar_suspeitos, acusar

def exibir_titulo():
    print("\n" + "=" * 50)
    print("      🍦 CRIMELATTO: O ENIGMA DOS SABORES 🍦")
    print("=" * 50)
    time.sleep(2)

def introducao():
    print("\n🌑 Bem-vindo(a)... se é que você está preparado para isso. Você entrou na Doce Latto, a sorveteria mais famosa, mas também a mais sombria da cidade. 🍨💀")
    time.sleep(3)
    print("Renomada por seus sabores únicos, a Doce Latto esconde um segredo gelado, um ingrediente raro e proibido: o Lustro. ❄️🕵️‍♂️")
    time.sleep(3)
    print("\nEsse misterioso Lustro dá vida aos sorvetes, permitindo que eles sintam, pensem... e, agora, agem. 🤖🍦")
    time.sleep(4)

    print("\nMas, na calada da noite, algo horrível aconteceu... ⚡💔")
    time.sleep(3)
    print("O Sr. Gelatelli, o excêntrico dono da sorveteria, foi encontrado sem vida em sua cozinha. O que aconteceu ali? O que ele sabia? 🏚️💭")
    time.sleep(4)

    print("\nOs sorvetes tomaram vida... e agora, um deles pode ser o assassino que silenciou Gelatelli. ❄️🔪")
    time.sleep(3)
    print("Você consegue desvendar esse enigma gelado antes que tudo se derreta em um mar de mentiras e mistérios? O tempo está contra você. ⏳")
    time.sleep(4)

def iniciar_jogo(sorvetes):
    culpado = random.choice(sorvetes)['nome_sorvete']
    print(f"\n🕵️‍♂️ O culpado foi determinado nas sombras... mas não se engane, nada é o que parece. Boa sorte em descobrir a verdade! 🔎❄️")

    while True:
        print("\n🌑 As sombras espreitam enquanto você pondera sobre o que fazer a seguir... 🌙👀")
        print("1. 🧩 Investigar a cena do crime")
        print("2. 🍦 Interrogar os sorvetes suspeitos")
        print("3. 📝 Analisar as pistas coletadas")
        print("4. ⚖️ Acusar um suspeito")
        print("5. 🚪 Sair... mas lembre-se, o mistério pode não ter fim.")

        escolha = input("\nDigite sua escolha: ")

        if escolha == "1":
            print("\n🔍 O ar está denso e gelado. Você avança lentamente, seu coração bate mais rápido enquanto examina a cena do crime. O silêncio é palpável, mas os detalhes começam a falar. ❄️👀")
            investigar_cena_crime()
        elif escolha == "2":
            print("\n🍦 Os suspeitos observam com olhos vazios e corações gelados. Cada um tem algo a esconder... será que você conseguirá extrair as verdades congeladas? ❄️🕵️‍♂️")
            interrogar_suspeitos(sorvetes)
        elif escolha == "3":
            print("\n📜 O caos está ao seu redor, mas se souber conectar as pistas certas, a verdade poderá se revelar... ou você poderá se afundar ainda mais nas sombras. 🌑🔍")
            mostrar_pistas()
        elif escolha == "4":
            print("\n⚖️ Você sente o peso da decisão. Acusar um inocente ou apontar o culpado? Não se engane, a linha entre a verdade e a mentira é tênue... 👁️⚖️")
            suspeito = input("Digite o nome do sorvete que você quer acusar: 🍦🔪")
            resultado = acusar(suspeito, culpado)
            print(resultado)
        elif escolha == "5":
            print("\n👋 Você se afasta da Doce Latto... mas a sombra do mistério ainda paira sobre você. A resposta pode nunca ser revelada. 🏚️👀")
            time.sleep(3)
            print("Saindo do jogo... ou será que você realmente saiu? 🔒🌑")
            time.sleep(3)
            break
        else:
            print("\n❌ Opção inválida... ou será que você escolheu errado? Escolha um número entre 1 e 5. 💭🔎")

if __name__ == "__main__":
    caminho_csv = "sorvetes.csv"
    sorvetes = carregar_sorvetes(caminho_csv)

    exibir_titulo()
    introducao()
    iniciar_jogo(sorvetes)