import csv
import time
import random

def carregar_sorvetes(caminho_csv):
    with open(caminho_csv, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo, delimiter=';')
        next(leitor_csv)

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

def interrogar_suspeitos(suspeitos):
    respostas = {
        "Moranguinho": "🍓 Moranguinho: \"Eu não faria mal a ninguém! Estava no fundo do freezer, como sempre... Por que todos desconfiam de mim? Talvez seja o medo de ser um sabor tão comum...\" 😰",
        "Bauni": "🍦 Bauni: \"Tão suave quanto meu gosto, sempre fiquei fora de confusão. Por que alguém suspeitaria de mim? Tudo que eu queria era continuar vivendo em paz, mas agora... não sei mais o que pensar.\" 😢",
        "Nocci": "🌰 Nocci: \"Humm... As pessoas tendem a subestimar o sabor das nozes, mas quem me conhece sabe que sou... paciente. No entanto, uma coisa é certa, se eu quisesse, poderia esconder segredos muito bem.\" 🤔",
        "Limone": "🍋 Limone: \"Ah, a liberdade... Sempre foi tudo que eu quis. Fugir dessa sorveteria e explorar o mundo lá fora. Mas matar? Isso seria extremo até para mim. No entanto... as circunstâncias nos mudam.\" 😓",
        "Pistacho": "🥜 Pistacho: \"Lustro... eu entendo os riscos mais do que qualquer outro. Esse ingrediente não é apenas mágico... ele é perigoso. Se mal utilizado, pode fazer qualquer um cometer atos impensáveis. Mas não fui eu... ou fui?\" 😶",
        "Caramella": "🍬 Caramella: \"Todos nós temos nossos segredos, mas alguns são mais doces do que outros. O Sr. Gelatelli sabia demais, e talvez tenha se envolvido com algo maior do que ele poderia controlar. Mas é claro... eu jamais seria tão imprudente.\" 😏",
        "Mentolado": "🌿 Mentolado: \"Você realmente acha que eu, o mais frio e controlado de todos, teria algo a ver com isso? Interessante. Mas cuidado... o frio muitas vezes esconde verdades sombrias.\" 🧐"
    }

    print("\n👀 Você começa a interrogar os suspeitos. Cada um tem algo a dizer, mas será que todos estão dizendo a verdade?")
    for suspeito in suspeitos:
        print(f"\n🍨 {suspeito} responde:")
        print(respostas[suspeito])
        time.sleep(3)

if __name__ == "__main__":
    caminho_csv = "sorvetes.csv"
    sorvetes = carregar_sorvetes(caminho_csv)
    mostrar_pistas()
    suspeitos = ["Moranguinho", "Bauni", "Nocci", "Limone", "Pistacho", "Caramella", "Mentolado"]
    interrogar_suspeitos(suspeitos)