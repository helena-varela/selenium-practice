from selenium import webdriver
from selenium.webdriver.common.by import By

# Exibe a Tabela Estática Completa
driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html")
linhas = driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr')
for linha in linhas:
    colunas = linha.find_elements(By.TAG_NAME, "td")
    print([coluna.text for coluna in colunas])
driver.quit()