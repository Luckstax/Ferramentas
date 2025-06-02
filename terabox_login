from playwright.sync_api import sync_playwright
import time
import json

def obter_token_terabox(email, senha):
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        pagina = navegador.new_page()
        pagina.goto("https://www.terabox.com")

        # Clicar em login
        pagina.click("text=Sign In")  # Pode ajustar se não funcionar
        time.sleep(3)

        # Preencher campos
        pagina.fill("input[type='text']", email)
        pagina.fill("input[type='password']", senha)
        pagina.click("button[type='submit']")

        # Esperar login completo
        pagina.wait_for_timeout(5000)

        cookies = pagina.context.cookies()
        navegador.close()

        for cookie in cookies:
            if cookie['name'] == 'BDUSS':
                return cookie['value']

        raise Exception("Token BDUSS não encontrado.")

if __name__ == "__main__":
    email = input("Email do TeraBox: ")
    senha = input("Senha do TeraBox: ")
    token = obter_token_terabox(email, senha)

    with open("config.json", "w") as f:
        json.dump({"BDUSS": token}, f)

    print("Token salvo em config.json")
