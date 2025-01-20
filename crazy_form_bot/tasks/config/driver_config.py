from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from global_config import config

# Configuración del driver de Firefox
driver_path = config.get("botData").get("driverPath")  # Ruta al geckodriver
service = Service(driver_path)
options = Options()

# Crear una instancia de WebDriver
driver = webdriver.Firefox(service=service, options=options)
driver.maximize_window()
