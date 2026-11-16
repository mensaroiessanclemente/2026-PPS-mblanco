from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time


class TestApp(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        options = webdriver.ChromeOptions()

        # executa Chrome sen mostrar a xanela gráfica
        # options.add_argument("--headless=new")

        # gardar o navegador como atributo da clase (cls)
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)  # Agardar 5 segundos

        cls.driver.quit()
        super().tearDownClass()

    def test_admin_page(self):
        self.driver.get(self.live_server_url + "/admin/")
        print("Título:", self.driver.title)

        # Comprobar o título da páxina
        self.assertIn("Log in | Django site admin", self.driver.title)
