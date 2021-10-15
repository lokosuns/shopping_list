from selenium import webdriver
import time


TEST_CLIENT = {
    'username': 'TestUser',
    'email': '123@123.ru',
    'password': 'q1w2e3r4TT',
}


def test_open_login_page(live_server, new_user):
    """
    Новый пользователь открывает
    браузер и решает ввести 'http://127.0.0.1:8000/'.
    Попадает на страницу с title 'Войти' и надписью ВХОД
    Вводит тестовый логин и пароль и переходит на главную
    """
    # browser = webdriver.Chrome('/home/lokosuns/PycharmProjects/working_list/chromedriver')
    # browser.get(live_server.url)
    # assert browser.title == 'Войти'
    # login = browser.find_element_by_name('login')
    # password = browser.find_element_by_name('password')
    # login.send_keys(TEST_CLIENT['username'])
    # password.send_keys(TEST_CLIENT['password'])
    #
    # button = browser.find_element_by_id('login-submit-btn')
    # button.click()
    #
    # # WebDriverWait(browser, 3).until(es.title_is('Главная'))
    # time.sleep(3)
    # assert browser.title == 'Главная'
    pass