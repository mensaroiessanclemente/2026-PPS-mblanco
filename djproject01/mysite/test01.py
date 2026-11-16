# módulo para controlar o navegador
from selenium import webdriver

# permite esperar a que certa condición ocorra antes de continuar. Axuda con certos elementos que poden tardar tempo en cargarse
from selenium.webdriver.support.ui import WebDriverWait

# proporciona condicións predefinidas que pode usar WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# módulo para localizar elementos HTML
from selenium.webdriver.common.by import By

import time

# iniciar Chrome con opcións básicas
options = webdriver.ChromeOptions()

# para que chrome se manteña aberto cando remate o proceso, se non se envía o comando quit
options.add_experimental_option("detach", True)

# non se mostra o navegador
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Crear unha espera máxima de 10 segundos
wait = WebDriverWait(driver, 10)

# acceder ao título da páxina
title = driver.title
print("Page title:", title)

# tempo de espera por se hai elementos que non están dispoñibles inmediatamente
driver.implicitly_wait(0.5)

time.sleep(3)

# acceder á caixa de texto polo atributo name
text_box = driver.find_element(by=By.NAME, value="my-text")

# escribir na caixa de texto
text_box.send_keys("Selenium")

time.sleep(3)

# acceder ao botón mediante selector CSS
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# facer click no botón e enviar o formulario
submit_button.click()

# Agardar a que apareza o título "Web form"
wait.until(EC.title_contains("Web form"))

# acceder ao elemento con ID especificado
message = driver.find_element(by=By.ID, value="message")
text = message.text

print("Confirmation message:", text)

# driver.quit()
