from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def weathersearch():
    print('Загружаем драйвер...')
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    print('Драйвер загружен')

    print('Ищем погоду...')
    driver.get('https://yandex.ru/pogoda/moscow')
    city = driver.find_element(By.XPATH, '//*[@id="main_title"]').text
    pogoda1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/a').text
    pogoda2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div[6]').text
    pogoda = (pogoda1 + '\n' + pogoda2).split('\n')

    print('\nПогода в', city)
    pogodastring = 'Температура: ' + pogoda[0] + ' (ощущается ' + pogoda[3] + ')' + \
                   '\nНебо: ' + pogoda[1] + \
                   '\nВетер: ' + pogoda[4] + \
                   '\nВлажность: ' + pogoda[5] + \
                   '\nДавление: ' + pogoda[6]
    print(pogodastring)
    driver.close()
    return pogodastring
