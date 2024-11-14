import time


from selenium import webdriver


from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By








import re


#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()
    #говорим WebDriver каждый элемент искать 5 секунд.
    # путь до страницы
    driver.get('https://erikdark.github.io/QA_autotest_16/')






    # ниже пишем свой код
   
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'price1')))


    WebDriverWait(driver,15).until(EC.text_to_be_present_in_element((By.ID,'price1'),'550'))


    driver.find_element(By.ID,'buyButton1').click()


    if driver.find_element(By.ID,'message1').text == 'Вы успешно купили автомобиль!':
        print('ok')
    else:
        print('ne okey')


   


   
    # конец блока с моим кодом




#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()
