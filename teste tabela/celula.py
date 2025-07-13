from selenium import webdriver
from selenium.webdriver.common.by import By

# Tabela Estática
driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html")
celula = driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td[3]')
print(f"Conteúdo da Célula: {celula.text}") 
driver.quit()