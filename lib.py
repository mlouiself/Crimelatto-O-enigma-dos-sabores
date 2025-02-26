import csv
import time
import random

def carregar_sorvetes(caminho_csv):
    sorvetes = []
    with open(caminho_csv, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo, delimiter=';')
        next(leitor_csv)
        for linha in leitor_csv:
            sabor_sorvete = linha[0]
            nome_sorvete = linha[1]
            aparencia = linha[2]
            consciencia = linha[3]
            quantidade_lustro = linha[4]
            personalidade = linha[5]
            personalidade_oculta = linha[6]
            nivel_derretimento = linha[7]
            freezer = linha[8]
            sorvetes.append({
                'sabor_sorvete': sabor_sorvete,
                'nome_sorvete': nome_sorvete,
                'aparencia': aparencia,
                'consciencia': consciencia,
                'quantidade_lustro': quantidade_lustro,
                'personalidade': personalidade,
                'personalidade_oculta': personalidade_oculta,
                'nivel_derretimento': nivel_derretimento,
                'freezer': freezer
            })
    return sorvetes

def mostrar_pistas():
    pistas = [
        "👣 Pegadas congeladas: As marcas parecem de alguém que tentou fugir apressadamente do freezer. O gelo estalava como se algo terrível tivesse acontecido lá dentro... Mas quem fugiria com tanto desespero?",
        "💧 Manchas de sorvete derretido: Um rastro pegajoso se estende pelo chão da cozinha, misturando sabores e cheiros. Cada gota parece contar uma história... mas será que é a história certa?",
        "🥄 Colher metálica torta: Jogada no chão, a colher ainda brilha sob a luz fraca. Foi dobrada por algo ou alguém com muita força... Como se estivesse envolvida em algo mais do que apenas servir sorvete.",
        "❄️  Fragmentos de sorvete congelado: Espalhados como cacos de vidro, pequenos pedaços de sorvete estão por toda parte. Mas não há sinais de luta... Eles foram deixados ali por propósito ou descuido?"
    ]
    print("\n🔍 Pistas misteriosas encontradas na cena do crime:")
    for pista in pistas:
        print(f"- {pista}")
        time.sleep(3)

def interrogar_suspeitos(sorvetes):
    respostas = {
        "Bauni🍦": "🍦 Bauni: \"Tão suave quanto meu gosto, sempre fiquei fora de confusão. Por que alguém suspeitaria de mim? Tudo que eu queria era continuar vivendo em paz, mas agora... não sei mais o que pensar.\" 😢",
        "Moranguinho🍓": "🍓 Moranguinho: \"Eu não faria mal a ninguém! Estava no fundo do freezer, como sempre... Por que todos desconfiam de mim? Talvez seja o medo de ser um sabor tão comum...\" 😰",
        "Mentolado🍃🍫": "🍃🍫 Mentolado: \"Você realmente acha que eu, o mais frio e controlado de todos, teria algo a ver com isso? Interessante. Mas cuidado... o frio muitas vezes esconde verdades sombrias.\" 🧐",
        "Nocci🌰": "🌰 Nocci: \"Humm... As pessoas tendem a subestimar o sabor das nozes, mas quem me conhece sabe que sou... paciente. No entanto, uma coisa é certa, se eu quisesse, poderia esconder segredos muito bem.\" 🤔",
        "Caramella🍯": "🍯 Caramella: \"Todos nós temos nossos segredos, mas alguns são mais doces do que outros. O Sr. Gelatelli sabia demais, e talvez tenha se envolvido com algo maior do que ele poderia controlar. Mas é claro... eu jamais seria tão imprudente.\" 😏",
        "Pistacho🌰": "🌰 Pistacho: \"Lustro... eu entendo os riscos mais do que qualquer outro. Esse ingrediente não é apenas mágico... ele é perigoso. Se mal utilizado, pode fazer qualquer um cometer atos impensáveis. Mas não fui eu... ou fui?\" 😶",
        "Limone🍋": "🍋 Limone: \"Ah, a liberdade... Sempre foi tudo que eu quis. Fugir dessa sorveteria e explorar o mundo lá fora. Mas matar? Isso seria extremo até para mim. No entanto... as circunstâncias nos mudam.\" 😓"
    }

    print("\n👀 Você começa a interrogar os suspeitos. Cada um tem algo a dizer, mas será que todos estão dizendo a verdade?")
    for sorvete in sorvetes:
        nome = sorvete['nome_sorvete']
        if nome == "Choco🍫":
            print(f"\n🍫 {nome} não pode responder, pois está fora de cena.")
        elif nome in respostas:
            print(f"\n🍨 {nome} responde:")
            print(respostas[nome])
        else:
            print(f"\n🍨 {nome} não tem nada a dizer.")
        time.sleep(3)

def investigar_cena_crime():
    print("\n🕵️‍♂️ A porta da cozinha range suavemente ao ser empurrada. O som parece o lamento de um espírito aprisionado, ecoando pela casa como um aviso. Você entra lentamente, e o ar, gelado e espesso, parece engolir seus pensamentos. O cheiro... algo ácido, algo doce, mas de um doce amargo, como o último suspiro de uma alma perdida.")
    time.sleep(4)

    print("\n🔍 O ambiente está silencioso demais, como se o tempo tivesse parado ali, congelado. Cada respiração sua parece um som invasivo, quebrando o silêncio mortal que toma conta do lugar. A luz fraca que emana de uma lâmpada suja no teto não oferece consolo — ela apenas ilumina o caos que foi deixado para trás. O que aconteceu aqui? Por que Gelatelli e Chocolate tiveram que morrer? A resposta está em cada detalhe, esperando para ser descoberta...")
    time.sleep(4)

    print("\n👀 Ao olhar ao redor, a visão se torna turva, como se a própria realidade estivesse distorcida. Há algo de errado com cada canto, cada sombra. O ar gélido parece pulsar com uma energia invisível, uma força que você não consegue compreender. Mas sente. E ela te observa, te espera. O que o assassino deixou para trás? O que ele esqueceu?")
    time.sleep(4)

    mostrar_pistas()

    print("\n🔎 O silêncio, denso e opressor, torna-se ainda mais palpável à medida que você observa cada objeto com mais atenção. Uma sensação de incomodidade começa a crescer, como se algo estivesse se movendo nas sombras, observando suas ações. Você não está mais sozinho aqui. O ar pesado carrega consigo uma presença que se esconde, aguardando o momento certo para se revelar.")
    time.sleep(4)

    print("\n💭 O cheiro do Lustro, doce e misterioso, começa a se infiltrar mais fundo em sua mente. Cada pista que você observa parece ter sido deixada de propósito, como se estivesse sendo guiado para algo maior. Mas o que? O Lustro foi a chave que deu vida a esses sorvetes... mas até que ponto ele controla suas mentes? O que Gelatelli sabia? E por que o Chocolate foi silenciado tão rapidamente?")
    time.sleep(4)

    print("\n🌫️  O frio ao seu redor parece aumentar a cada passo, como se a própria casa estivesse se tornando um cadáver congelado. A atmosfera, carregada de segredos não ditos, começa a sufocar suas inspirações. Tudo ali parece ser um reflexo distorcido da realidade, como se as paredes estivessem atentas a cada movimento seu. Algo está errado, mas você não consegue identificar o quê. A resposta está ao seu alcance, mas ela não virá facilmente. A verdade... ou a mentira? A linha entre elas é tênue.")
    time.sleep(4)

    print("\n⚡ O jogo é mais antigo do que você imagina. O Lustro, esse ingrediente mágico, pode estar manipulando você, os sorvetes, todos. Mas o que ele realmente quer? Quem realmente está no controle? Você sente como se estivesse se afundando em um pesadelo, onde nada é o que parece e onde qualquer passo errado pode te afundar ainda mais nas profundezas da mentira e do desespero.")
    time.sleep(4)

    print("\n❗ O perigo está mais perto do que você imagina. Cada respiração que você dá parece mais pesada, cada pensamento mais sombrio. Você sabe que está perto, mas está começando a questionar se quer mesmo saber a verdade. Algumas coisas, talvez, devam ficar enterradas no gelo. Você continua... ou se afasta do abismo que está prestes a engolir tudo?")
    time.sleep(4)

def acusar(suspeito, culpado):
    if suspeito == culpado:
        return (f"💥 O ar parece congelar por um instante. Você aponta para {suspeito}, e uma sensação pesada toma conta de você, como se o tempo parasse. "
                f"Uma sombra se afasta das paredes e a verdade, até então escondida nas sombras, se revela. "
                f"Com um suspiro final, você sente um arrepio percorrer sua espinha. Você acertou. {suspeito} era o culpado o tempo todo... e a justiça foi feita. "
                f"Mas será que a paz será alcançada? Ou isso é apenas o começo de um novo mistério? 🕯️")
    else:
        return (f"❌ O ar se torna denso, e um calafrio percorre sua coluna. Você acusa {suspeito}, mas ao olhar nos olhos do verdadeiro culpado, "
                f"uma estranha sensação de desconforto toma conta de você. Algo não está certo. O silêncio da sala cresce, como se as paredes estivessem "
                f"rindo de sua acusação falha. {suspeito} não era o culpado... Ou será que ele ainda guarda segredos mais profundos? O jogo continua... 🕳️")

if __name__ == "__main__":
    caminho_csv = "sorvetes.csv"
    sorvetes = carregar_sorvetes(caminho_csv)
    
    investigar_cena_crime()
    
    mostrar_pistas()
    
    interrogar_suspeitos(sorvetes)