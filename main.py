import time
import random
from lib import valores_perigosos, carregar_sorvetes, investigar_cena_crime, mostrar_pistas, interrogar_suspeitos, acusar


def exibir_titulo():
    print("\n" + "-" * 50)
    print("      🍦 Crimelatto: O enigma dos sabores 🍦")
    print("-" * 50)
    time.sleep(2)

def introducao():
    print("\n🍨 Bem-vindo(a) a Doce Latto, a sorveteria mais enigmática da cidade... 🍨")
    time.sleep(3)
    print("Famosa pelos sabores exóticos, mas poucos sabem sobre o ingrediente secreto e proibido que ela esconde: o Lustro. ✨")
    time.sleep(3)
    print("\nEsse ingrediente raro tem o poder de dar vida aos sorvetes, permitindo que eles... pensem, sintam... e agora, talvez... ajam? 👀")
    time.sleep(4)
    
    print("\nNa noite passada, um crime misterioso abalou o coração da Doce Latto. 💔") 
    time.sleep(3)
    print("O excêntrico dono, Sr. Gelatelli, foi encontrado sem vida em sua cozinha, um enigma congelado no ar. 🥶")
    time.sleep(4)

    print("\nMas... algo estranho aconteceu... os sorvetes ganharam vida. E agora, entre eles, pode estar o assassino do Sr. Gelatelli. 🔪👁️")
    time.sleep(3)
    print("Você consegue desvendar esse mistério antes que tudo se derreta em um mar de mentiras e segredos? ⏳")
    time.sleep(6)

def iniciar_jogo(sorvetes):
    culpado = random.choice(sorvetes)['nome_sorvete']
    print(f"\n- A verdade está nas sombras, oculta nos corações congelados. Mas, cuidado... as aparências podem enganar. Boa sorte, detetive. 🔍")

    while True:
        print("\nO mistério cresce, as sombras sussurram. O que você fará a seguir? 🌑")
        print("1. 🧩 Investigar a cena do crime")
        print("2. 🍦 Interrogar os sorvetes suspeitos")
        print("3. 📝 Analisar as pistas coletadas")
        print("4. 💣 Analisar tabela de valores perigosos")
        print("5. ⚖️  Acusar um suspeito")
        print("6. 🚪 Sair do jogo")

        escolha = input("\nDigite sua escolha: ")

        if escolha == "1":
            print("\n❄️ O ar está pesado, quase congelante. Cada passo ecoa no silêncio, mas entre as sombras... algo começa a se revelar. ❄️")
            investigar_cena_crime()
        elif escolha == "2":
            print("\n🍦 Os sorvetes falam com vozes congeladas... será que você conseguirá extrair as verdades ocultas entre as camadas de gelo? 🍦")
            interrogar_suspeitos(sorvetes)
        elif escolha == "3":
            print("\n🔍 As pistas estão espalhadas, como fragmentos de um sonho congelado. Conecte-as, e a verdade poderá surgir... 🔍")
            mostrar_pistas()
        elif escolha == "4":
            print("\n 🚨 ALERTA! Os seguintes valores ultrapassam os limites seguros. Proceda com cautela... 🚨")
            valores_perigosos()
        elif escolha == "5":
            print("\n🔪 A tensão é palpável... o peso da acusação. Você está prestes a decidir: quem entre os sorvetes é o culpado? ⚖️")
            suspeito = input("Digite o nome do sorvete que você deseja acusar: ")
            resultado = acusar(suspeito, culpado)
            print(resultado)
        elif escolha == "6":
            print("\nVocê se afasta da Doce Latto, mas a neblina do mistério ainda envolve sua mente. O enigma permanece sem solução. 💀")
            time.sleep(3)
            print("Saindo do jogo... a escuridão aguarda sua próxima visita. 🕯️")
            time.sleep(3)
            break
        else:
            print("\n❌ Opção inválida! Escolha um número entre 1 e 5, ou se perderá na escuridão. ❌")

if __name__ == "__main__":
    caminho_csv = "sorvetes.csv"
    sorvetes = carregar_sorvetes(caminho_csv)

    exibir_titulo()
    introducao()
    iniciar_jogo(sorvetes)