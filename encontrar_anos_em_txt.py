import re

livro= "Camilo-A_Brasileira_de_Prazins.md"
txt=open(livro, encoding="utf-8").read()

def encontrar_anos(txt, output_file="anos.txt"):
    # Divide o texto em capítulos usando '#' como marcador de início de capítulo
    capitulos = re.split(r'#', txt)
    
    # Expressão regular para encontrar sequências de 4 números (anos)
    padrao_ano = r'\b\d{4}\b'

    with open(output_file, 'w', encoding='utf-8') as output:
        for i, capitulo in enumerate(capitulos[1:], start=1):
            anos_encontrados = re.findall(padrao_ano, capitulo)
            if anos_encontrados:
                output.write(f"Anos encontrados no Capítulo {i}: {anos_encontrados}\n")

encontrar_anos(txt)


