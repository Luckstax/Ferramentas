import pyautogui as py
from time import sleep
from playwright.sync_api import sync_playwright

def apertar(tecla):
    py.press(tecla)

with sync_playwright() as p:
    navegador = p.firefox.launch(headless=False)
    contexto = navegador.new_context(
        viewport={"width": 1920, "height": 1080}
    )
    pagina = contexto.new_page()

    # ← Aqui você coloca o fechamento automático de pop-ups
    pagina.on("popup", lambda popup: popup.close())

    pagina.goto("https://jennaortega.net/gallery/thumbnails.php?album=315#google_vignette")

    # Aguarda carregamento da página e elementos visuais
    sleep(5)

    # Navegar até a primeira foto
    pos_foto = (469, 1005)
    py.moveTo(pos_foto)
    py.click()


    # Aguarda a imagem abrir (pode ajustar o tempo se necessário)
    sleep(5)

    # Clique direito sobre a imagem para abrir o menu
    pos_imagem = (1023, 454)  # ajuste se necessário
    py.moveTo(pos_imagem)
    py.click(button='right')
    sleep(1)

    # Navega até "Salvar imagem como..."
    apertar('down')
    apertar('down')
    apertar('enter')
    apertar('tab')
    apertar('tab')
    apertar('tab')
    apertar('enter')
    sleep(7)  # tempo para janela "Salvar como" aparecer
    pos_prox = (1497, 115)  # ajuste se necessário
    py.moveTo(pos_prox)
    py.click()

