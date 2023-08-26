from selenium import webdriver
from selenium.webdriver.common.by import By

import time

#не получается использовать из-за окна после перехода на главную страницу
#метод быстро находит кнопку и кликает по ней, но она ещё недоступна
#так что будут дебильные временные задержки
# а ещё даже assert не отрабатывает
#browser.implicitly_wait(5)

#fun

def test_tags_fun():
    #Это, чтобы язык браузера установить на англ (почему то русский язык по умолчанию
    #открывается через selenium, хотя вроде убрал рус яз из настроек)
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    browser = webdriver.Chrome(options=options)

    #Адрес сайта, который открываем
    link = "https://playhop.com/"
    browser.get(link)
    time.sleep(3)

    # находим кнопку и нажимаем
    # и что, всегда надо нажимать эту кнопку??
    # теперь она пропала. надо впн обновить?
    button = browser.find_element(By.XPATH,"//*[text()='Consent']")

    #исключение, если формы согласия не будет
    #это не работает, так как надо по другому писать
    #подумать позже
    #assert "Consent" in button.text, "Форма согласия отсутствует"

    button.click()
    # задержка
    time.sleep(2)

    #клик по кнопке с тегом
    button1 = browser.find_element(By.XPATH, "//*[text()='fun']")

    #этим скроллим до нужного элемента
    #можно использовать submit()  вместо click()
    #в таком случае кнопка нажмётся даже если не видна на странице
    #но это вроде не надо
    button1.location_once_scrolled_into_view

    button1.click()
    time.sleep(2)

    #проверка что действительно открылась страница c нужным текстом в заголовке
    title = browser.find_element(By.CLASS_NAME, "section-header__text")
    assert "fun" in title.text, "Переход не выполнен, либо заголовок не найден"
    time.sleep(2)

    browser.quit()

#test_tags_fun()
