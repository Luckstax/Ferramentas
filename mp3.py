import whisper
import os

# Caminho da pasta com os áudios
pasta_audios = r"C:\Users\Lucas\Music\diario"

# Carrega o modelo Whisper (pode usar "base", "small", "medium", "large", etc.)
modelo = whisper.load_model("large")

# Verifica cada arquivo na pasta
for nome_arquivo in os.listdir(pasta_audios):
    if nome_arquivo.lower().endswith((".mp3", ".wav", ".m4a", ".ogg")):
        caminho_audio = os.path.join(pasta_audios, nome_arquivo)

        print(f"Transcrevendo: {nome_arquivo}")
        resultado = modelo.transcribe(caminho_audio, language='Portuguese')

        # Nome do arquivo de saída (mesmo nome do áudio, mas com .txt)
        nome_txt = os.path.splitext(nome_arquivo)[0] + ".txt"
        caminho_txt = os.path.join(pasta_audios, nome_txt)

        # Salva a transcrição
        with open(caminho_txt, "w", encoding="utf-8") as f:
            f.write(resultado["text"])

        print(f"Transcrição salva em: {caminho_txt}\n")

print("Todas as transcrições foram concluídas.")
