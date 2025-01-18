from global_config import config
from utils.read_excel import ReadExcel
from tasks.fill_form import FillForm

import time

print("Iniciando proceso de lectura de archivo excel...")

# Crear una instancia de ReadExcel
read_excel = ReadExcel(config.get("processData").get("excelPath"))

# Obtener los datos del archivo excel
data = read_excel.read()

print("Iniciando proceso de llenado de formularios...")

# Crear una instancia de FillForm
fill_form = FillForm(config.get("processData").get("url"))

# Inicializar el driver
fill_form.initialize_driver()

# Inicializar el reto
fill_form.initialize_challenge()

# Iterar sobre los datos obtenidos del archivo excel
for row in data:
    # Ejecutar el método run
    fill_form.run(row)

# Esperar resultados (opcional)
time.sleep(5)

# Cerrar el driver
# fill_form.close_driver()

print("Proceso finalizado.")
