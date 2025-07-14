from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import os
from dotenv import load_dotenv

load_dotenv()

usuario = os.getenv("SIGAA_USER")
senha = os.getenv("SIGAA_PASS")
if not usuario or not senha:
    raise ValueError("Variáveis SIGAA_USER e SIGAA_PASS não foram encontradas no .env")

driver = webdriver.Chrome()

try:
    driver.get("https://autenticacao.ufrn.br/sso-server/login?service=https%3A%2F%2Fsigaa.ufrn.br%2Fsigaa%2Flogin%2Fcas")
    driver.find_element(By.ID, "username").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(senha)
    driver.find_element(By.CLASS_NAME, "btn-primary").click()

    try:
        WebDriverWait(driver, 5).until(
            EC.url_contains("sigaa.ufrn.br/sigaa/portais/discente/discente.jsf")
        )
        print("✅ Login realizado com sucesso!")
    except:
        erro = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "login-error"))
        )
        print(f"❌ Falha no Login: \n{erro.text}")

    time.sleep(3)

except Exception as e:
    print(f"Erro inesperado: {str(e)}")

finally:
    driver.quit()
    print("Navegador fechado.")