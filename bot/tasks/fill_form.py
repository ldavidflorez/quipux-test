from selenium.webdriver.common.by import By

from tasks.config.driver_config import driver


class FillForm:
    def __init__(self, url):
        self.url = url

    def initialize_driver(self):
        # Configuración de tiempos de espera
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(10)

        # Abrir Google
        driver.get(self.url)

    def close_driver(self):
        driver.quit()

    def initialize_challenge(self):
        # Clic en Start Challenge
        start_button = driver.find_element(
            By.XPATH,
            "//*[contains(text(), 'Start Challenge')]",
        )
        start_button.click()

    def run(self, data):
        try:
            # Rellenar el campo "Name"
            name_field = driver.find_element(By.ID, "nombres")
            name_field.send_keys(data.get("Nombres"))

            # Rellenar el campo "Last Name"
            last_name_field = driver.find_element(By.ID, "apellidos")
            last_name_field.send_keys(data.get("Apellidos"))

            # Rellenar campo "Country"
            country_field = driver.find_element(By.ID, "pais")
            country_field.send_keys(data.get("Pais"))

            # Rellenar campo "Email"
            email_field = driver.find_element(By.ID, "email")
            email_field.send_keys(data.get("Email"))

            # Rellenar campo "Company"
            company_field = driver.find_element(By.ID, "empresa")
            company_field.send_keys(data.get("Empresa"))

            # Rellenar campo "Phone"
            phone_field = driver.find_element(By.ID, "numero")
            phone_field.send_keys(data.get("Numero"))

            # Rellenar campo "Web"
            web_field = driver.find_element(By.ID, "web")
            web_field.send_keys(data.get("Web"))

            # Hacer clic en el botón "Submit"
            submit_button = driver.find_element(
                By.XPATH,
                "//*[contains(text(), 'Submit')]",
            )
            submit_button.click()

        except Exception as e:
            print(f"Error: {e}")
