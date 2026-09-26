"""Quiz de perguntas e respostas executado no terminal."""

PERGUNTAS = [
    {
        "enunciado": "Qual linguagem estamos usando neste programa?",
        "opcoes": ["Java", "Python", "C#", "PHP"],
        "resposta": 2,
    },
    {
        "enunciado": "Quanto é 7 x 8?",
        "opcoes": ["54", "56", "64", "48"],
        "resposta": 2,
    },
    {
        "enunciado": "Qual destes é um sistema operacional?",
        "opcoes": ["Windows", "Google", "Python", "HTML"],
        "resposta": 1,
    },
]


def ler_resposta(total_opcoes):
    """Lê uma alternativa válida, de 1 até total_opcoes."""
    while True:
        resposta = input("Sua resposta: ").strip()
        if resposta.isdigit() and 1 <= int(resposta) <= total_opcoes:
            return int(resposta)
        print(f"Digite apenas um número de 1 a {total_opcoes}.")


def executar_quiz():
    pontos = 0
    total = len(PERGUNTAS)

    print("=" * 40)
    print("       BEM-VINDO AO QUIZ!")
    print("=" * 40)

    for numero, pergunta in enumerate(PERGUNTAS, start=1):
        print(f"\nPergunta {numero} de {total}")
        print(pergunta["enunciado"])

        for indice, opcao in enumerate(pergunta["opcoes"], start=1):
            print(f"{indice}) {opcao}")

        resposta = ler_resposta(len(pergunta["opcoes"]))

        if resposta == pergunta["resposta"]:
            pontos += 1
            print("Correto!")
        else:
            correta = pergunta["opcoes"][pergunta["resposta"] - 1]
            print(f"Resposta incorreta. A correta era: {correta}.")

    percentual = pontos / total * 100
    print("\n" + "=" * 40)
    print(f"Resultado final: {pontos} de {total} ({percentual:.0f}%)")
    print("=" * 40)


if __name__ == "__main__":
    executar_quiz()