import json
import pandas as pd

def gerar_planilha_seguindo(arquivo_json):
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        # Acessando a lista correta dentro do JSON do Instagram
        # O arquivo 'following.json' geralmente tem uma chave principal chamada 'relationships_following'
        if isinstance(dados, dict) and 'relationships_following' in dados:
            itens = dados['relationships_following']
        else:
            itens = dados

        lista_seguindo = []
        
        for item in itens:
            if 'string_list_data' in item:
                for info in item['string_list_data']:
                    lista_seguindo.append({
                        'Usuário': info.get('value', 'N/A'),
                        'Link': info.get('href', ''),
                        'Timestamp': info.get('timestamp', 0)
                    })
        
        df = pd.DataFrame(lista_seguindo)

        # Converte o timestamp para data legível de forma segura
        if not df.empty:
            df['Data'] = pd.to_datetime(df['Timestamp'], unit='s', errors='coerce')
            # Remove a coluna original de segundos para ficar limpo
            df = df.drop(columns=['Timestamp'])

        nome_saida = 'seguindo_instagram.xlsx'
        df.to_excel(nome_saida, index=False)
        
        print(f"Sucesso! {len(df)} usuários exportados para '{nome_saida}'.")

    except Exception as e:
        print(f"Erro ao processar: {e}")

if __name__ == "__main__":
    gerar_planilha_seguindo('following.json')