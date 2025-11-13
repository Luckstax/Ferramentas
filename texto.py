import os
from pathlib import Path

def gerar_prompts_local(caminho_pasta, tag_personagem):
    caminho = Path(caminho_pasta)
    if not caminho.exists():
        print(f"❌ Pasta '{caminho_pasta}' não encontrada.")
        return

    # Filtra imagens
    imagens = [f for f in caminho.iterdir() if f.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]]

    if not imagens:
        print("❌ Nenhuma imagem encontrada na pasta.")
        return

    print(f"✅ {len(imagens)} imagens encontradas. Criando arquivos .txt...")

    for img_path in imagens:
        # Aqui você deve colocar o prompt gerado pelo WD14 Tagger
        # Para simplificar, vamos criar um prompt de exemplo vazio
        # No uso real, substitua 'prompt_exemplo' pelo output do WD14 Tagger
        prompt_exemplo = "example_tag1, example_tag2, example_tag3"

        # Adiciona a tag do personagem no início
        prompt_final = f"{tag_personagem}, {prompt_exemplo}"

        txt_path = img_path.with_suffix(".txt")
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(prompt_final)

    print(f"✅ Concluído! Arquivos .txt criados em: {caminho_pasta}")


if __name__ == "__main__":
    print("=== WD14 LoRA Tagger Local (PyCharm) ===")
    pasta = input("Digite o caminho da pasta com as imagens: ").strip('"')
    tag = input("Digite a tag do personagem (ex: jenna_ortega): ").strip().replace(" ", "_")
    gerar_prompts_local(pasta, tag)
