# Máscara de CPF e Telefone em Excel

Este projeto contém um script em Python para **normalizar e formatar colunas de CPF e telefone** em arquivos Excel (`.xlsx`).  
Ele permite que você leia uma planilha, aplique a máscara correta e salve o resultado em um novo arquivo.

---

## Funcionalidades

- Aplicar máscara de **CPF** no formato `000.000.000-00`.
- Aplicar máscara de **telefone** no formato `(DD) 9XXXX-XXXX`.
- Filtrar automaticamente valores inválidos:
  - CPFs que não têm 11 dígitos
  - Telefones que não têm 13 dígitos
- Evita warnings comuns do Pandas usando `.loc`.
- Tratamento de erros:
  - Arquivo inexistente
  - Planilha inexistente
  - Coluna inexistente
  - Opção inválida de máscara

---

## Pré-requisitos

- Python 3.10 ou superior
- Bibliotecas Python:
  - pandas
  - openpyxl

Instale usando pip:

```bash
pip install pandas openpyxl


mascara-formatacao/
│
├─ README.md
├─ requirements.txt
├─ mascara_de_cpf.py
├─ exemplos/
│   ├─ 28-11.xlsx
│   └─ 28-11_formatada.xlsx
└─ docs/  (opcional, para prints ou documentação extra)



Uso

Clone ou baixe o projeto.

Abra o terminal na pasta do projeto.

Ative o virtualenv (opcional, mas recomendado):

Windows PowerShell:

.\venv\Scripts\Activate.ps1


Linux/macOS:

source venv/bin/activate


Execute o script:

python mascara_de_cpf.py


Siga as instruções interativas:

Informe o caminho do arquivo Excel (.xlsx)

Informe o nome da aba/planilha

Informe o nome da coluna que deseja formatar

Escolha a máscara: cpf ou telefone

O arquivo será salvo automaticamente na mesma pasta com o nome:

<nome_do_arquivo>_formatada.xlsx

Exemplo de execução
Digite o caminho do arquivo: exemplos/28-11.xlsx
Digite o nome da planilha: Sheet1
Digite o nome da variavel: Phone 1 - Value
A mascara é telefone ou cpf?: telefone
Arquivo salvo como 28-11_formatada.xlsx
