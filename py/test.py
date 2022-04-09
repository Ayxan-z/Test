from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import xlsxwriter


def getCompanyInfo(link):
    driver.get(link)

    company_name = driver.find_element(by=By.CLASS_NAME, value="item-title").text
    addresses = driver.find_element(by=By.CLASS_NAME, value="lh-md")
    addresses = addresses.text.split('\n')
    if len(addresses) == 2:
        address, city = addresses
        postcode = 'None'

    else: address, postcode, city = addresses

    sleep(1)
    driver.find_element(by=By.ID, value='telephone-entreprise').click()
    sleep(0.3)
    telephone = driver.find_element(by=By.CLASS_NAME, value="phone-container").text
    
    while not telephone:
        driver.get(link)
        sleep(1)
        driver.find_element(by=By.ID, value='telephone-entreprise').click()
        sleep(0.3)
        telephone = driver.find_element(by=By.CLASS_NAME, value="phone-container").text
    
    box = driver.find_element(by=By.CLASS_NAME, value='md-down-mb-lg')
    box = box.text.split('\n')

    s = ''
    for i in box:
        if i[0] == '-':
            s += '|'.join(i.split('\n')) + '|'
    
    return [company_name, s, address, postcode, city, telephone]

def writeToXlsx(column_names, column_title, data, file_name):
    with xlsxwriter.Workbook(file_name + '.xlsx') as workbook:
        worksheet = workbook.add_worksheet()
        
        for i, cn in enumerate(column_names):
            worksheet.write(f'{cn}1', column_title[i])
        
        for i, d in enumerate(data):
            for j, cn in enumerate(column_names):
                worksheet.write(f'{cn}{i+2}', d[j])

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver_path = "C:\\Users\\shahs\\Documents\\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    driver.get("https://www.qualit-enr.org/annuaire/?type=installateurs-photovoltaique&ville=01")

    link_data = driver.find_elements(by=By.CLASS_NAME, value="results-item")

    links = [i.get_attribute('href') for i in link_data]
    driver.get(links[0])

    data = []
    for link in links:
        data.append(getCompanyInfo(link))

    column_names = ['A','B','C','D','E','F']
    column_title = ['Company Name', 'Nos compétences', 'Address', 'Postcode', 'City', 'Telephone']
    writeToXlsx(column_names, column_title, data, 'qualit-enr')