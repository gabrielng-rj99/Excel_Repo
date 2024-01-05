import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your chromedriver executable
chromedriver_path = 'C:\\Python\\chromedriver-win64\\chromedriver.exe'

# Create a Service object with the path to chromedriver
service = Service(chromedriver_path)

# Create a new instance of the Chrome driver with the Service object
driver = webdriver.Chrome(service=service)

# Set the URL of the website
url = 'https://www.mazusoft.com.br/mega/resultados.php'

# Navigate to the website
driver.get(url)

# Wait for the dropdowns to be present
dropdown1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'con_inicial'))
)
dropdown2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'con_final'))
)

# Set the dropdown values to 1 and 2656
driver.execute_script("arguments[0].value = '1';", dropdown1)

# Locate and click the button by its class
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'btn'))
)
button.click()

# Add a delay to allow the content to load
driver.implicitly_wait(5)

# Wait for the selected numbers to be present
selected_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'lotoBg'))
)

# Extract and print the selected numbers
selected_numbers = []
MegaSenaMatrix = []


for element in selected_elements:
    temp = int(element.text)
    selected_numbers.append(temp)
    del temp
    
    if len(selected_numbers)==6:
        MegaSenaMatrix += [selected_numbers]
        del selected_numbers
        selected_numbers = []
        
    else:
        pass
    
# Keep the browser window open
driver.quit()


column_names = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6']

# Create a dictionary from the lists
data_dict = {col: values for col, values in zip(column_names, zip(*MegaSenaMatrix))}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data_dict)

# Specify the Excel file path
excel_file_path = 'D:\\!!!!!!Projetos\\Análise de Dados e Programação\\Análise de Dados - Mega Sena\\output.xlsx'

# Use ExcelWriter to write the DataFrame to an Excel file
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    # Write the DataFrame to the Excel file
    df.to_excel(writer, sheet_name='Sheet1', index=False)

# Print a message indicating successful export
print('''_____________________________________________________\n
The Data Extraction Was Successful
_____________________________________________________''')
