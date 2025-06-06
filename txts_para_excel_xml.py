import os
from xml.etree.ElementTree import Element, SubElement, ElementTree
import xml.dom.minidom as minidom

def encontrar_txts(pasta_raiz):
    arquivos_txt = []
    for raiz, _, arquivos in os.walk(pasta_raiz):
        for arquivo in arquivos:
            if arquivo.lower().endswith('.txt'):
                arquivos_txt.append(os.path.join(raiz, arquivo))
    return arquivos_txt

def criar_xml_com_abas(lista_de_txts):
    # Estrutura base do Excel XML
    workbook = Element('Workbook', {
        'xmlns': "urn:schemas-microsoft-com:office:spreadsheet",
        'xmlns:o': "urn:schemas-microsoft-com:office:office",
        'xmlns:x': "urn:schemas-microsoft-com:office:excel",
        'xmlns:ss': "urn:schemas-microsoft-com:office:spreadsheet"
    })

    for caminho_txt in lista_de_txts:
        nome_base = os.path.basename(caminho_txt)
        nome_aba = os.path.splitext(nome_base)[0]

        worksheet = SubElement(workbook, 'Worksheet', {'ss:Name': nome_aba})
        table = SubElement(worksheet, 'Table')

        with open(caminho_txt, 'r', encoding='utf-8') as f:
            for linha in f:
                row = SubElement(table, 'Row')
                celulas = linha.rstrip('\n').split('\t')  # separa por tabulação
                for valor in celulas:
                    cell = SubElement(row, 'Cell')
                    data = SubElement(cell, 'Data', {'ss:Type': 'String'})
                    data.text = valor

    return workbook

def salvar_xml(workbook, nome_arquivo='saida.xml'):
    xml_str = ElementTree(workbook)
    xml_str.write(nome_arquivo, encoding='utf-8', xml_declaration=True)
    # Opcional: gerar versão "bonita" com indentação
    dom = minidom.parse(nome_arquivo)
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(dom.toprettyxml(indent="  "))

if __name__ == '__main__':
    pasta_alvo = input("Informe o caminho da pasta com os arquivos .txt: ").strip()
    arquivos_txt = encontrar_txts(pasta_alvo)
    
    if not arquivos_txt:
        print("Nenhum arquivo .txt encontrado.")
    else:
        xml = criar_xml_com_abas(arquivos_txt)
        salvar_xml(xml, 'resultado_excel.xml')
        print(f"Arquivo XML gerado com sucesso: resultado_excel.xml")
