# módulo para controlar el navegador
from selenium import webdriver

# permite esperar a que aparezcan los elementos
from selenium.webdriver.support.ui import WebDriverWait, Select

# condiciones para las esperas
from selenium.webdriver.support import expected_conditions as EC

# módulo para localizar elementos HTML
from selenium.webdriver.common.by import By

import time

# crear las opciones básicas del navegador
options = webdriver.ChromeOptions()

# iniciar Chrome
driver = webdriver.Chrome(options=options)

try:

    # acceder a la página de SauceDemo
    driver.get("https://www.saucedemo.com/")

    # esperar 5 segundos para ver la página
    time.sleep(5)

    # crear una espera máxima de 10 segundos
    wait = WebDriverWait(driver, 10)

    # localizar el campo de usuario
    username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

    # introducir el usuario
    username.send_keys("standard_user")

    # esperar 2 segundos
    time.sleep(2)

    # localizar el campo de contraseña
    password = driver.find_element(By.ID, "password")

    # introducir la contraseña
    password.send_keys("secret_sauce")

    # esperar 2 segundos
    time.sleep(2)

    # localizar y pulsar el botón de login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # esperar a que aparezcan los productos
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))

    print("Inicio de sesión correcto")

    # esperar 3 segundos para ver los productos
    time.sleep(3)

    # localizar el desplegable de ordenación
    sort_products = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))

    # ordenar los productos de menor a mayor precio
    sort_products.select_by_value("lohi")

    # esperar 3 segundos para ver los productos ordenados
    time.sleep(3)

    # obtener todos los productos
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")

    # mostrar nombre y precio de cada producto
    print("\nProductos ordenados por precio (menor a mayor):")

    for product in products:

        # obtener el nombre
        name = product.find_element(By.CLASS_NAME, "inventory_item_name").text

        # obtener el precio
        price = product.find_element(By.CLASS_NAME, "inventory_item_price").text

        # mostrar por consola
        print("Nombre:", name, "| Precio:", price)

    # esperar 5 segundos antes de cerrar
    time.sleep(5)

finally:

    # cerrar el navegador
    driver.quit()
