while True:
    escolha = input("🕵‍♂ O que você deseja fazer, Detetive? ")

    if escolha == '1':
        print("🔦 Você acende sua lanterna e a cena do crime surge em seu caminho... Pegadas congeladas levam ao inesperado.")
        print("💀 O corpo do Sr. Gelatelli, o excêntrico dono da sorveteria, está caído ao lado de um saco de Lustro derramado.")
        print("😱 Seu rosto congelado em uma expressão de choque e medo... Ele viu o assassino antes do fim.")
        print("❄ Manchas de derretimento no chão, um vidro rachado no freezer, e uma colher metálica torta sugerem que algo frio e mortal passou por ali.")
    elif escolha == '2':
        print("🗣 As vozes dos sorvetes ecoam no freezer... Quem será o traidor? Quem fala a verdade?")
        nome_sorvete = input("🍨 Qual sorvete você deseja interrogar? ")
        função_exibir_sorvete = (nome_sorvete)
    elif escolha == '3':
        print("🍦❄ O freezer range ao abrir... Um sopro frio te arrepia a espinha. Algo ou alguém esteve aqui.")
        nome_sorvete = input("📦 Qual sorvete do estoque você quer investigar? ")
        exibir_sorvete = (nome_sorvete)
    elif escolha == '4':
        print("🧭 O vento gelado sussurra segredos e pistas ao seu redor... Você segue o chamado da verdade.")
    elif escolha == '5':
        print("🚪 O som da porta da sorveteria fechando atrás de você é quase silencioso... Mas o enigma permanece.")
        break
    else:
            print("🌀 Hmm... Opção inválida. O frio está confundindo sua mente?. Tente novamente.")

def exibir_menu():
    print("🧊🍨✨ ~~~ Bem-vindo à Sorveteria Doce Latto ~~~ ✨🍨🧊")
    print("💀 Um crime gelado à espreita... desvendará você esse enigma sombrio? 💀")
    print("❄❄❄==========================================❄❄❄")
    print("1 🔍 *INVESTIGAR A CENA DO CRIME*: Mergulhe nas sombras e procure pistas.")
    print("2 🗣 *INTERROGAR OS SUSPEITOS*: Cada sorvete tem uma história... e segredos.")
    print("3 🍦 *EXAMINAR O FREEZER*: O estoque guarda segredos. Escolha com cuidado.")
    print("4 🧭 *SEGUIR UMA PISTA SOMBRIA*: O enigma se adensa. Algo te chama...")
    print("5 🚪 *DEIXAR A SORVETERIA*: Fugir ou voltar para resolver? A escolha é sua.")
    print("❄❄❄==========================================❄❄❄")