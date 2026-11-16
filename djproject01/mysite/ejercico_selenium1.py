from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

try:

    # Abrir la página
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Esperar 5 segundos para poder ver la página
    time.sleep(5)

    wait = WebDriverWait(driver, 10)

    print("Page title:", driver.title)

    # Localizar la caja de texto
    text_box = wait.until(EC.visibility_of_element_located((By.NAME, "my-text")))

    # Escribir en la caja de texto
    text_box.send_keys("Selenium")

    # Esperar 3 segundos para ver el texto escrito
    time.sleep(3)

    # Localizar el botón
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button")))

    # Esperar antes de enviar el formulario
    time.sleep(3)

    # Enviar el formulario
    submit_button.click()

    # Esperar el mensaje de confirmación
    message = wait.until(EC.visibility_of_element_located((By.ID, "message")))

    print("Confirmation message:", message.text)

    # Mantener el resultado visible
    time.sleep(5)

finally:
    driver.quit()
