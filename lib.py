import time
import csv
import random

def imprimir_lentamente(texto, velocidade=0.03):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(velocidade)
    print()

def carregar_sorvetes():
    sorvetes = []
    try:
        arquivo = open('sorvetes.csv', 'r', encoding='utf-8')
        leitor = csv.reader(arquivo, delimiter=';')
        next(leitor)
        
        for linha in leitor:
            sorvete = {
                "sabor_sorvete": linha[0],
                "nome_sorvete": linha[1],
                "aparencia": linha[2],
                "consciencia": linha[3],
                "quantidade_lustro": linha[4],
                "personalidade": linha[5],
                "personalidade_oculta": linha[6],
                "nivel_derretimento": linha[7],
                "freezer": linha[8]
            }
            sorvetes.append(sorvete)
        
        arquivo.close()
    except FileNotFoundError:
        print("Erro: O arquivo 'sorvetes.csv' não foi encontrado.")
        exit(1)
    
    return sorvetes

def exibir_introducao():
    print("\n" + "="*50)
    print("CRIMELATTO: O ENIGMA DOS SABORES".center(50))
    print("="*50 + "\n")

    historia = [
        "Na pacata e renomada sorveteria Doce Latto, os sabores não são apenas deliciosos – eles têm consciência.",
        "Criados com o segredo mais bem guardado da cidade, o Lustro, um ingrediente mágico que lhes confere vida.",
        "No entanto, um dia, o Sr. Gelatelli, dono da loja, é encontrado morto.",
        "E, para surpresa de todos, o sabor Chocolate, um dos mais populares, também foi assassinado.",
        "Como um investigador contratado, você deve descobrir a verdade por trás desse crime gelado.",
        "Mas antes de começar sua investigação, você deve assinar um contrato de trabalho que garante a segurança dos segredos da CrimeLatto."
    ]
    
    for linha in historia:
        imprimir_lentamente(linha)
    
    nome_investigador = input("\nQual é o seu nome, investigador? ")
    print(f"\nBem-vindo, {nome_investigador}! Vamos prosseguir com a assinatura do contrato.")

    contrato = f"""
    +---------------------------------------------------------+
    |                   CONTRATO DE INVESTIGAÇÃO              |
    |                      Sorveteria Doce Latto             |
    +---------------------------------------------------------+

    Parabéns! Você foi contratado(a) como investigador(a) da
    Sorveteria Doce Latto, o lugar mais enigmático e delicioso da cidade.

    Aqui, os sabores são mais do que simples delícias – eles possuem segredos,
    e você foi escolhido(a) para desvendá-los. Sua missão é clara: resolver
    o mistério por trás do assassinato de Sr. Gelatelli e do sabor Chocolate,
    sem jamais revelar o que descobrir.

    Ao assinar este contrato, você concorda com os seguintes termos:

    1. *Sigilo Absoluto*: Toda e qualquer informação sobre a Doce Latto, seus sabores,
       ingredientes secretos e acontecimentos internos deve permanecer em segredo.

    2. *Proibição de Questionar o Lustro*: O Lustro é o ingrediente misterioso e vital
       que dá vida aos nossos sorvetes. Sua origem e seus efeitos são secretos e não podem ser questionados.

    3. *Dever de Resolução*: Como investigador(a), você deve usar sua habilidade de dedução
       para resolver o crime. Isso inclui examinar pistas e interrogar suspeitos.

    4. *Regras para Solução do Crime*:
       - Você deve examinar pelo menos 3 pistas antes de fazer uma acusação.
       - É obrigatório interrogar pelo menos 2 suspeitos.
       - Utilize as informações coletadas para formular sua acusação.
       - Caso faça uma acusação sem seguir as regras, sua pontuação será reduzida.

    5. *Consequências*: Quebrar este contrato resultará em severas penalidades,
       incluindo, mas não se limitando, a derretimento instantâneo de seus próprios segredos.

    Assine abaixo para confirmar sua aceitação:

    [Nome do Investigador]: {nome_investigador}

    [Data]: {time.strftime('%d/%m/%Y')}

    +---------------------------------------------------------+
    | Atenção: Este contrato é vinculante e irrevogável.       |
    | Boa sorte, você precisará dela!                         |
    +---------------------------------------------------------+
    """
    
    for linha in contrato.split("\n"):
        imprimir_lentamente(linha, velocidade=0.02)

    input("\nPressione ENTER para continuar...")

def exibir_cena_crime():
    print("\n" + "="*50)
    print("A CENA DO CRIME".center(50))
    print("="*50 + "\n")

    descricao = [
        "Você chega à sorveteria CrimeLatto. A polícia já isolou o local.",
        "O corpo do Sr. Gelatelli foi encontrado na cozinha, ao lado de um saco de Lustro derramado.",
        "Em um freezer, encontra-se o que restou do sabor Chocolate.",
        "As pistas incluem pegadas geladas, manchas de derretimento, um vidro rachado e uma colher torta.",
        "Como investigador, sua missão é descobrir o culpado antes que os segredos da CrimeLatto sejam perdidos para sempre."
    ]

    for linha in descricao:
        imprimir_lentamente(linha)
    
    input("\nPressione ENTER para continuar...")

def examinar_pista(pista, culpado):
    if pista == "1":
        return examinar_pegadas(culpado)
    elif pista == "2":
        return examinar_lustro(culpado)
    elif pista == "3":
        return examinar_colher(culpado)
    elif pista == "4":
        return examinar_vidro(culpado)
    else:
        return 0

def examinar_pegadas(culpado):
    imprimir_lentamente("Você examina as pegadas geladas no chão...")
    if culpado["nivel_derretimento"] == "Rápido⚡":
        imprimir_lentamente("As pegadas derreteram rápido.")
        return 1
    else:
        imprimir_lentamente("As pegadas ainda estão bem definidas.")
        return 2

def examinar_lustro(culpado):
    imprimir_lentamente("Você examina o recipiente de Lustro...")
    if culpado["quantidade_lustro"] == "Alta⬆️":
        imprimir_lentamente("Tem marcas de mãos pequenas.")
        return 2
    else:
        imprimir_lentamente("Parece ter sido aberto à força.")
        return 1

def examinar_colher(culpado):
    imprimir_lentamente("Você examina a colher metálica torta...")
    if "Freezer 2" in culpado["freezer"]:
        imprimir_lentamente("Tem resíduos do Freezer 2.")
        return 2
    else:
        imprimir_lentamente("Não dá para determinar a origem dos resíduos.")
        return 1

def examinar_vidro(culpado):
    imprimir_lentamente("Você examina a rachadura no vidro...")
    if "fuga" in culpado["personalidade_oculta"].lower():
        imprimir_lentamente("Foi feita de dentro para fora.")
        return 2
    else:
        imprimir_lentamente("Não está claro se foi quebrado de dentro para fora.")
        return 1

def interrogar_suspeito(suspeito, culpado):
    imprimir_lentamente(f"\nVocê interroga {suspeito['nome_sorvete']} ({suspeito['sabor_sorvete']})...")
    
    perguntas = [
        "Onde você estava na noite do crime?",
        "O que sabe sobre o Lustro?",
        "Qual era sua relação com Chocolate?",
        "O que acha que aconteceu com Gelatelli?"
    ]
    
    respostas = {
        "Onde você estava na noite do crime?": {
            "Bauni🍦": "Eu estava no meu freezer, como sempre. Não sou de me mover muito!",
            "Moranguinho🍓": "Eu estava me divertindo, mas não sou de ficar presa a horários!",
            "Mentolado🍃🍫": "Estava em silêncio, como sempre. O que mais poderia fazer?",
            "Nocci🌰": "Refletindo sobre a vida e o significado do Lustro.",
            "Caramella🍯": "Ah, querido, eu estava apenas esperando o momento certo para brilhar.",
            "Pistacho🌰": "Estava em um experimento, tentando entender o Lustro melhor.",
            "Limone🍋": "Eu estava me preparando para uma explosão de sabor, como sempre!"
        },
        "O que sabe sobre o Lustro?": {
            "Bauni🍦": "Lustro é algo que confere poder, mas não sei muito além disso. É... perigoso.",
            "Moranguinho🍓": "Ouvi rumores, mas não confio em ninguém aqui.",
            "Mentolado🍃🍫": "O Lustro é um mistério, e eu prefiro não me envolver.",
            "Nocci🌰": "O Lustro é fascinante, mas também perigoso. Conheço seus segredos.",
            "Caramella🍯": "Ah, o Lustro... é uma delícia, mas tem suas armadilhas.",
            "Pistacho🌰": "O Lustro é a chave para muitos segredos. Estou sempre estudando.",
            "Limone🍋": "Lustro? É o que dá sabor à vida, mas também pode ser traiçoeiro."
        },
        "Qual era sua relação com Chocolate?": {
            "Bauni🍦": "Chocolate sempre foi o favorito. Eu sempre estive à sombra dele.",
            "Moranguinho🍓": "Ele era popular, mas eu não me importava. Eu sou única!",
            "Mentolado🍃🍫": "Chocolate era um rival, mas eu preferia ficar na minha.",
            "Nocci🌰": "Tínhamos uma relação de respeito, mas sempre havia competição.",
            "Caramella🍯": "Ah, Chocolate... sempre tão doce e tão ingênuo.",
            "Pistacho🌰": "Chocolate era um enigma, sempre intrigante.",
            "Limone🍋": "Chocolate? Ele era bom, mas eu sou o verdadeiro sabor!"
        },
        "O que acha que aconteceu com Gelatelli?": {
            "Bauni🍦": "Gelatelli era muito próximo do segredo do Lustro. Acho que ele sabia demais.",
            "Moranguinho🍓": "Ele estava sempre no meio de tudo. Não me surpreenderia se soubesse algo.",
            "Mentolado🍃🍫": "Gelatelli era um mistério, e seu destino é igualmente enigmático.",
            "Nocci🌰": "Gelatelli era sábio, mas os segredos podem ser perigosos.",
            "Caramella🍯": "Gelatelli provavelmente se meteu em algo que não deveria.",
            "Pistacho🌰": "Ele estava sempre buscando conhecimento. Isso pode ter sido sua ruína.",
            "Limone🍋": "Gelatelli? Ele era um jogador, e os jogadores às vezes perdem."
        }
    }

    for i, pergunta in enumerate(perguntas, 1):
        print(f"{i}. {pergunta}")
    
    escolha = int(input("Escolha uma pergunta (digite o número): ")) - 1
    pergunta_escolhida = perguntas[escolha]
    resposta_escolhida = respostas[pergunta_escolhida][suspeito['nome_sorvete']]
    
    imprimir_lentamente(f"Você pergunta: {pergunta_escolhida}")
    time.sleep(0.5)
    imprimir_lentamente(f"O interrogado responde: {resposta_escolhida}")
    
    if suspeito == culpado:
        return 3
    else:
        return 1

def revelar_culpado(acusado, culpado, pontos):
    print("\n" + "="*50)
    print("REVELAÇÃO FINAL".center(50))
    print("="*50 + "\n")

    if acusado == culpado:
        imprimir_lentamente(f"Você acusa {acusado['nome_sorvete']}...")
        imprimir_lentamente("Ele tenta fugir, mas é tarde demais!")
        imprimir_lentamente("O assassino confessa!")
        imprimir_lentamente(f"Motivo: {culpado['personalidade_oculta']}")
        imprimir_lentamente(f"Pontuação final: {pontos} pontos.")
    else:
        imprimir_lentamente(f"Você acusa {acusado['nome_sorvete']}...")
        imprimir_lentamente("Mas o verdadeiro culpado escapa!")
        imprimir_lentamente(f"O assassino era {culpado['nome_sorvete']} ({culpado['sabor_sorvete']}).")
        imprimir_lentamente(f"Motivo: {culpado['personalidade_oculta']}")
        imprimir_lentamente(f"Pontuação final: {pontos - 5} pontos.")

    print("\nFIM DE JOGO!")