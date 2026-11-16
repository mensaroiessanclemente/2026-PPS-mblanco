from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time
import os


from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class MySeleniumTests(StaticLiveServerTestCase):
    # cargar unha BD de test
    fixtures = ["testdb.json"]

    # execútase unha vez antes dos tests da clase
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        options = webdriver.ChromeOptions()
        if os.environ.get("CHROME_HEADLESS") == "1":
            options.add_argument("--headless=new")

        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(10)

    # pecha o navegador e o servidor
    @classmethod
    def tearDownClass(cls):
        # cerrar o navegador

        cls.driver.quit()
        super().tearDownClass()

    def test_login(self):
        # acceder á páxina de login de admin
        self.driver.get("%s%s" % (self.live_server_url, "/admin/login/"))

        # comprobar que o título da páxina é o esperado
        self.assertEqual(self.driver.title, "Log in | Django site admin")
        time.sleep(3)
        # introducir os datos de login e pulsar o botón “Log in” para entrar
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys("admin")
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys("tiburon6")
        self.driver.find_element(By.XPATH, '//input[@value="Log in"]').click()
        time.sleep(5)

        # comprobar se se conseguiu entrar
        self.assertEqual(self.driver.title, "Site administration | Django site admin")
