import time
import csv
from tabulate import tabulate

def imprimir_lentamente(texto, velocidade=0.03):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(velocidade)
    print()

dados = [
    ["Consciência", "Acima de 50%"],
    ["Quantidade de lustro", "Média - Alta"],
    ["Nível de derretimento", "Médio - Rápido"]
]

def valores_perigosos():
    print(tabulate(dados, headers=["Parametro", "Valor"], tablefmt="grid"))

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
        "Na renomada sorveteria Doce Latto, os sabores não são apenas deliciosos – eles têm consciência.",
        "Criados com o segredo mais bem guardado da cidade, o Lustro, um ingrediente mágico que lhes confere vida.",
        "No entanto, um dia, o Sr. Gelatelli, dono da loja, é encontrado morto.",
        "E, para surpresa de todos, Choco, o sorvete sabor chocolate, um dos mais populares, também foi assassinado.",
        "Como um investigador contratado, você deve descobrir a verdade por trás desse crime gelado.",
        "Mas antes de começar sua investigação, você deve assinar um contrato de trabalho que garante a segurança dos segredos da Doce Latto."
    ]
    
    for linha in historia:
        imprimir_lentamente(linha)
    
    nome_investigador = input("\nQual é o seu nome, investigador? ")
    print(f"\nBem-vindo, {nome_investigador}! Vamos prosseguir com a assinatura do contrato.")

    contrato = f"""
    +-------------------------------------------------+
    |              CONTRATO DE INVESTIGAÇÃO           |
    |               Sorveteria Doce Latto             |
    +-------------------------------------------------+

    Parabéns! Você foi contratado(a) como investigador(a) da
    Sorveteria Doce Latto, o lugar mais enigmático e delicioso da cidade.

    Aqui, os sabores são mais do que simples delícias – eles possuem segredos,
    e você foi escolhido(a) para desvendá-los. Sua missão é clara: resolver
    o mistério por trás do assassinato de Sr. Gelatelli e Choco,
    sem jamais revelar o que descobrir.

    Ao assinar este contrato, você concorda com os seguintes termos:

    1. *Sigilo Absoluto*: Toda e qualquer informação sobre a Doce Latto, seus sabores,
       ingredientes secretos e acontecimentos internos deve permanecer em segredo.

    2. *Proibição de Questionar o Lustro*: O Lustro é o ingrediente misterioso e vital
       que dá vida aos nossos sorvetes. Sua origem e seus efeitos são secretos e não podem ser questionados.

    3. *Dever de Resolução*: Como investigador(a), você deve usar sua habilidade de dedução
       para resolver o crime. Isso inclui examinar pistas e interrogar suspeitos.

    4. *Consequências*: Quebrar este contrato resultará em severas penalidades,
       incluindo, mas não se limitando, a derretimento instantâneo de seus próprios segredos.

    Assine abaixo para confirmar sua aceitação:

    [Nome do Investigador]: {nome_investigador}

    [Data]: {time.strftime('%d/%m/%Y')}

    +---------------------------------------------------------+
    | Atenção: Este contrato é vinculante e irrevogável.      |
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
        "Você chega à sorveteria Doce Latto. A polícia já isolou o local.",
        "O corpo do Sr. Gelatelli foi encontrado na cozinha, ao lado de um saco de Lustro derramado.",
        "Em um freezer, encontra-se o que restou de Choco.",
        "As pistas incluem pegadas geladas, manchas de derretimento, um vidro rachado e uma colher torta.",
        "Como investigador, sua missão é descobrir o culpado antes que os segredos da Doce Latto sejam perdidos para sempre."
    ]

    for linha in descricao:
        imprimir_lentamente(linha)
    
    input("\nPressione ENTER para continuar...")

def examinar_pista(pista, culpado):
    if pista == "1":
        examinar_pegadas(culpado)
    elif pista == "2":
        examinar_lustro(culpado)
    elif pista == "3":
        examinar_colher(culpado)
    elif pista == "4":
        examinar_vidro(culpado)

def examinar_pegadas(culpado):
    imprimir_lentamente("Você examina as pegadas geladas no chão...")
    if culpado["nivel_derretimento"] == "Rápido⚡":
        imprimir_lentamente("As pegadas derreteram rápido.")
    else:
        imprimir_lentamente("As pegadas ainda estão bem definidas.")

def examinar_lustro(culpado):
    imprimir_lentamente("Você examina o recipiente de Lustro...")
    if culpado["quantidade_lustro"] == "Alta⬆️":
        imprimir_lentamente("Tem marcas de mãos pequenas.")
    else:
        imprimir_lentamente("Parece ter sido aberto à força.")

def examinar_colher(culpado):
    imprimir_lentamente("Você examina a colher metálica torta...")
    if "Freezer 2" in culpado["freezer"]:
        imprimir_lentamente("Tem resíduos do Freezer 2.")
    else:
        imprimir_lentamente("Não dá para determinar a origem dos resíduos.")

def examinar_vidro(culpado):
    imprimir_lentamente("Você examina a rachadura no vidro...")
    if "fuga" in culpado["personalidade_oculta"].lower():
        imprimir_lentamente("Foi feita de dentro para fora.")
    else:
        imprimir_lentamente("Não está claro se foi quebrado de dentro para fora.")

def interrogar_suspeito(suspeito, culpado):
    imprimir_lentamente(f"\nVocê interroga {suspeito['nome_sorvete']} ({suspeito['sabor_sorvete']})...")
    
    perguntas = [
        "Onde você estava na noite do crime?",
        "O que sabe sobre o Lustro?",
        "Qual era sua relação com Choco?",
        "O que acha que aconteceu com Sr. Gelatelli?"
    ]
    
    respostas = {
        "Onde você estava na noite do crime?": {
            "Bauni": "Eu estava no meu freezer, como sempre. Não sou de me mover muito!",
            "Moranguinho": "Eu estava me divertindo, mas não sou de ficar presa a horários!",
            "Mentolado": "Estava em silêncio, como sempre. O que mais poderia fazer?",
            "Nocci": "Refletindo sobre a vida e o significado do Lustro.",
            "Caramella": "Ah, querido, eu estava apenas esperando o momento certo para brilhar.",
            "Pistacho": "Estava em um experimento, tentando entender o Lustro melhor.",
            "Limone": "Eu estava me preparando para uma explosão de sabor, como sempre!"
        },
        "O que sabe sobre o Lustro?": {
            "Bauni": "Lustro é algo que confere poder, mas não sei muito além disso. É... perigoso.",
            "Moranguinho": "Ouvi rumores, mas não confio em ninguém aqui.",
            "Mentolado": "O Lustro é um mistério, e eu prefiro não me envolver.",
            "Nocci": "O Lustro é fascinante, mas também perigoso. Conheço seus segredos.",
            "Caramella": "Ah, o Lustro... é uma delícia, mas tem suas armadilhas.",
            "Pistacho": "O Lustro é a chave para muitos segredos. Estou sempre estudando.",
            "Limone": "Lustro? É o que dá sabor à vida, mas também pode ser traiçoeiro."
        },
        "Qual era sua relação com Chocolate?": {
            "Bauni": "Chocolate sempre foi o favorito. Eu sempre estive à sombra dele.",
            "Moranguinho": "Ele era popular, mas eu não me importava. Eu sou única!",
            "Mentolado": "Chocolate era um rival, mas eu preferia ficar na minha.",
            "Nocci": "Tínhamos uma relação de respeito, mas sempre havia competição.",
            "Caramella": "Ah, Chocolate... sempre tão doce e tão ingênuo.",
            "Pistacho": "Chocolate era um enigma, sempre intrigante.",
            "Limone": "Chocolate? Ele era bom, mas eu sou o verdadeiro sabor!"
        },
        "O que acha que aconteceu com Gelatelli?": {
            "Bauni": "Gelatelli era muito próximo do segredo do Lustro. Acho que ele sabia demais.",
            "Moranguinho": "Ele estava sempre no meio de tudo. Não me surpreenderia se soubesse algo.",
            "Mentolado": "Gelatelli era um mistério, e seu destino é igualmente enigmático.",
            "Nocci": "Gelatelli era sábio, mas os segredos podem ser perigosos.",
            "Caramella": "Gelatelli provavelmente se meteu em algo que não deveria.",
            "Pistacho": "Ele estava sempre buscando conhecimento. Isso pode ter sido sua ruína.",
            "Limone": "Gelatelli? Ele era um jogador, e os jogadores às vezes perdem."
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

def revelar_culpado(acusado, culpado):
    print("\n" + "="*50)
    print("REVELAÇÃO FINAL".center(50))
    print("="*50 + "\n")

    if acusado == culpado:
        imprimir_lentamente(f"Você aponta, com uma calma imperturbável, para {acusado['nome_sorvete']}...")
        imprimir_lentamente("O ar na sala congela. Um silêncio profundo e denso toma conta do ambiente.")
        imprimir_lentamente(f"{acusado['nome_sorvete']} vacila, seus olhos, antes tranquilos, agora cheios de incerteza.")
        imprimir_lentamente("Em um movimento desesperado, ele tenta fugir, mas algo o detém... A justiça não pode ser impedida.")
        imprimir_lentamente("O mistério se dissolve diante de você, como neve ao sol. Você trouxe a verdade à luz de Doce Latto!")
        print("\n✨ O ENIGMA FOI DESVENDADO. A JUSTIÇA TRIUNFOU! ✨")
        
        print("\n" + "="*50)
        print("FIM DE JOGO!".center(50))
        print("="*50)
        
    else:
        imprimir_lentamente(f"Você, confiante, aponta para {acusado['nome_sorvete']}, acreditando que a verdade está ao seu alcance...")
        imprimir_lentamente("Mas algo no ar faz o sangue gelar. Uma sensação de incerteza rasteja por sua espinha.")
        imprimir_lentamente("De repente, uma risada baixa e maquiavélica preenche o espaço. O eco da risada é como o vento em uma noite sombria.")
        imprimir_lentamente(f"{culpado['nome_sorvete']} emerge das sombras, seu sorriso sombrio refletindo uma vitória cruel.")
        imprimir_lentamente(f"«Você falhou, investigador... O verdadeiro culpado sou eu!»")
        imprimir_lentamente("Com uma risada final, o assassino desaparece na escuridão, deixando para trás apenas um rastro de gelo derretido.")
        print("\n💀 O ERRO FOI SEU! O CULPADO ESCAPOU, E O CRIME PERMANECE NO AR... 💀")
        
        print("\n" + "="*50)
        print("FIM DE JOGO!".center(50))
        print("="*50)