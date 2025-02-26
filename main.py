import time

def exibir_titulo():
    """Exibe o título do jogo"""
    print("\n" + "=" * 50)
    print("      🍦 CRIMELATTO: O ENIGMA DOS SABORES 🍦")
    print("=" * 50)
    time.sleep(2)

def introducao():
    """Exibe a introdução da história"""
    print("\nBem-vindo(a) a Doce Latto, a sorveteria mais famosa da cidade!")
    time.sleep(3)
    print("Renomada por seus sabores únicos, a Doce Latto guarda um segredo: o Lustro.")
    time.sleep(3)
    print("\nEste ingrediente especial dá vida aos sorvetes, permitindo que pensem, sintam...")
    time.sleep(3)
    print("E, como foi descoberto recentemente, ajam.")
    time.sleep(4)
    
    print("\nNa última noite, um crime chocante abalou a sorveteria.")
    print("O Sr. Gelatelli, o excêntrico dono do estabelecimento, foi encontrado morto em sua cozinha.")
    time.sleep(4)

    print("\nOs sorvetes ganharam vida... e agora, um deles pode ser um assassino.")
    time.sleep(3)
    print("Desvendará você esse enigma gelado?")
    time.sleep(4)

def iniciar_jogo():
    """Inicia o jogo e permite o jogador escolher como prosseguir"""
    while True:
        print("\nO que deseja fazer, investigador?")
        print("1. Investigar a cena do crime")
        print("2. Interrogar os sorvetes suspeitos")
        print("3. Analisar as pistas coletadas")
        print("4. Sair do jogo")

        escolha = input("\nDigite sua escolha: ")

        if escolha == "1":
            print("\n🔍 Você começa a analisar a cena do crime em busca de evidências...")
            time.sleep(4)
            # Aqui podemos chamar uma função que detalha as pistas da cena do crime
        elif escolha == "2":
            print("\n🍦 Cada sorvete tem uma história... e segredos.")
            time.sleep(4)
            # Aqui podemos criar uma função para as interrogações dos personagens
        elif escolha == "3":
            print("\n📜 Se conectar as pistas certas, a verdade começará a se revelar no meio do caos gelado...")
            time.sleep(4)
            # Aqui podemos criar um menu para o jogador revisar as evidências
        elif escolha == "4":
            print("\n👋 O investigador deixa a sorveteria... mas o mistério permanece sem solução.")
            time.sleep(3)
            print("Saindo do jogo...")
            time.sleep(3)
            break
        else:
            print("\nOpção inválida! Escolha um número entre 1 e 4.")

# Execução principal do jogo
if __name__ == "__main__":
    exibir_titulo()
    introducao()
    iniciar_jogo()