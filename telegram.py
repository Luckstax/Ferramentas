import os
from telegram import Bot

# CONFIGURAÇÕES
TOKEN = "SEU_TOKEN_DO_BOT"
CHAT_ID = "SEU_CHAT_ID"  # pode ser ID de grupo ou canal (@nomedocanal ou número)
PASTA = r"C:\caminho\da\sua\pasta"

def enviar_arquivos_em_ordem():
    bot = Bot(token=TOKEN)

    # Lista arquivos e ordena em ordem crescente
    arquivos = sorted(
        [f for f in os.listdir(PASTA) if os.path.isfile(os.path.join(PASTA, f))]
    )

    for nome_arquivo in arquivos:
        caminho = os.path.join(PASTA, nome_arquivo)
        print(f"Enviando: {nome_arquivo}")

        with open(caminho, "rb") as f:
            bot.send_document(chat_id=CHAT_ID, document=f)

    print("Todos os arquivos foram enviados.")

if __name__ == "__main__":
    enviar_arquivos_em_ordem()
