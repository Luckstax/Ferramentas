import pandas as pd
import os

#chamada de arquivo
arquivo = input("Digite o caminho do arquivo:")

try:
    planilha = input("Digite o nome da planilha:")
    df = pd.read_excel(arquivo, sheet_name=planilha)
except FileNotFoundError:
    print("Arquivo não encontrado")
    exit()
except ValueError:
    print("planilha não encontrada")
    exit()
            
variavel = input("digite o nome da variavel:").strip()

if variavel not in df.columns:
    print("Coluna não encontrada")
    exit()

#guardar nome para reutilizar
nome = os.path.splitext(os.path.basename(arquivo))[0]
saida = f"{nome}_formatada.xlsx"

#mascara para CPF
def cpf(df,coluna):
    df[coluna] =df[coluna].astype(str).str.replace(r"\D","",regex=True)
    df=df[df[coluna].str.len() == 11]
    df.loc[:,coluna] = df[coluna].str.replace(r"(\d{3})(\d{3})(\d{3})(\d{2})", r"\1.\2.\3-\4", regex=True)
    return df


#mascara para telefone
def telefone(df,coluna):
    df[coluna] =df[coluna].astype(str).str.replace(r"\D","",regex=True)
    df=df[df[coluna].str.len() == 13]
    df.loc[:,coluna] = df[coluna].str.replace(r"(\d{2})(\d{2})(\d{5})(\d{4})", r"(\1) \2 \3-\4", regex=True)
    return df



opcao = input ("a mascara é telefone ou cpf?:").strip().lower()

if opcao == "cpf":
    df=cpf(df,variavel)

elif opcao =="telefone":
    df=telefone(df,variavel)

else:
    print("opção invalida")    
    exit()



df.to_excel(saida, index = False)
print(f"arquivo salvo como {saida}")