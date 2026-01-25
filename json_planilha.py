import json
import pandas as pd

def extrair_dados(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    
    lista_limpa = []
    # O formato do Instagram pode variar, esse loop garante a captura correta
    for item in dados:
        if 'string_list_data' in item:
            user_data = item['string_list_data'][0]
            lista_limpa.append({
                'usuario': user_data['value'],
                'link': user_data['href'],
                'data': pd.to_datetime(user_data['timestamp'], unit='s')
            })
    return lista_limpa

# 1. Carregar os dados
try:
    seguidores = extrair_dados('followers_1.json')
    seguindo = extrair_dados('following.json')

    df_seguidores = pd.DataFrame(seguidores)
    df_seguindo = pd.DataFrame(seguindo)

    # 2. Identificar quem não te segue de volta
    # (Pessoas que você segue mas não estão na lista de seguidores)
    nao_seguem_de_volta = df_seguindo[~df_seguindo['usuario'].isin(df_seguidores['usuario'])]

    # 3. Exportar para Excel
    with pd.ExcelWriter('analise_instagram.xlsx') as writer:
        df_seguidores.to_sheet(writer, sheet_name='Seguidores', index=False)
        df_seguindo.to_sheet(writer, sheet_name='Seguindo', index=False)
        nao_seguem_de_volta.to_sheet(writer, sheet_name='Nao_me_seguem_de_volta', index=False)

    print("Sucesso! Planilha 'analise_instagram.xlsx' gerada.")

except FileNotFoundError:
    print("Erro: Certifique-se de que os arquivos .json estão na mesma pasta do script.")
