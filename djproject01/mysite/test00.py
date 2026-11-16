from selenium import webdriver
import time

# iniciar Chrome con opcións básicas
options = webdriver.ChromeOptions()

# para manter aberto chrome cando remate o proceso, se non se envía o comando quit
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")

print("Chrome está aberto.")

time.sleep(3)

print("O programa rematou.")
# driver.quit()
