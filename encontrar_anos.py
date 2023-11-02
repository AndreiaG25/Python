import re

livro= "Camilo-A_Brasileira_de_Prazins.md"
txt=open(livro, encoding="utf-8").read()

def encontrar_anos(txt):
    # Divide o texto em capítulos usando '#' como marcador de início de capítulo
    capitulos = re.split(r'#', txt)
    
    # Expressão regular para encontrar sequências de 4 números (anos)
    padrao_ano = r'\b\d{4}\b'

    for i, capitulo in enumerate(capitulos[1:], start=1):
        anos_encontrados = re.findall(padrao_ano, capitulo)
        if anos_encontrados:
            print(f"Anos encontrados no Capítulo {i}: {anos_encontrados}")

encontrar_anos(txt)

#A expressão regular padrao_ano = r'\b\d{4}\b' tem o seguinte significado:
#\b: Isso é chamado de "ancoragem de borda". O \b denota uma fronteira de palavra, indicando que a sequência de dígitos \d{4} deve ser uma palavra completa, ou seja, deve ser delimitada por caracteres que não são dígitos (como espaço em branco, pontuação, início/fim de linha etc.).
# \d{4}: Aqui, \d é um atalho para qualquer dígito de 0 a 9. O {4} indica que deve haver exatamente quatro dígitos consecutivos. Portanto, essa parte da expressão regular corresponde a uma sequência exata de quatro dígitos.
#Em resumo, a expressão regular '\b\d{4}\b' é usada para encontrar sequências de exatamente quatro dígitos (que geralmente representam anos, como "2023" ou "1999") e garante que essas sequências sejam palavras completas, não fazendo parte de outras palavras.