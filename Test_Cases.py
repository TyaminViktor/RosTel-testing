import pytest, itertools, time
from settings import valid_email, valid_password, valid_phone_number, valid_login, valid_ls
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(autouse=True)
def testing():
    pytest.engine = webdriver.Chrome('chromedriver.exe')
    pytest.engine.fullscreen_window()
    pytest.engine.maximize_window()
    pytest.engine.get('https://b2c.passport.rt.ru')
    WebDriverWait(pytest.engine, 90).until(EC.visibility_of_element_located((By.ID, "username")))
    yield
    pytest.engine.quit()

def test_TK_RosTel_001():
    header_name, copyrighter, tab_phone, tab_mail, tab_login, tab_ls, btn_enter, btn_forgot, btn_code_enter, btn_register, username_field, password_field, label = None, None, None, None, None, None, None, None, None, None, None, None, None
    # Поиск элементов страницы
    try:
        header_name = pytest.engine.find_element(By.CLASS_NAME, "main-header__logo")
        copyrighter = pytest.engine.find_element(By.CLASS_NAME, "rt-footer-copyright")
        label = pytest.engine.find_element(By.CLASS_NAME, "what-is__title")
        tab_phone = pytest.engine.find_element(By.ID, "t-btn-tab-phone")
        tab_mail = pytest.engine.find_element(By.ID, "t-btn-tab-mail")
        tab_login = pytest.engine.find_element(By.ID, "t-btn-tab-login")
        tab_ls = pytest.engine.find_element(By.ID, "t-btn-tab-ls")
        btn_enter = pytest.engine.find_element(By.ID, "kc-login")
        btn_forgot = pytest.engine.find_element(By.ID, "forgot_password")
        btn_register = pytest.engine.find_element(By.ID, "kc-register")
        username_field = pytest.engine.find_element(By.ID, "username")
        password_field = pytest.engine.find_element(By.ID, "password")
        btn_code_enter = pytest.engine.find_element(By.ID, "back_to_otp_btn")
    except BaseException:
        print("\n Один из искомых элементов не найден")
    # Поиск местоположения поля авторизации
    auth_container = pytest.engine.find_element(By.CLASS_NAME, "login-form-container")
    auth_side = auth_container.find_element(By.XPATH, "parent::*").get_attribute("id")
    # Проверка наличия основных элементов на странице
    assert btn_enter != None
    assert btn_forgot != None
    assert btn_register != None
    assert username_field != None
    assert password_field != None
    assert tab_login != None
    assert tab_mail != None
    assert tab_phone != None
    assert tab_ls != None
    assert btn_code_enter != None
    assert header_name != None
    assert label != None
    assert copyrighter != None
    # Проверка положения поля авторизации
    assert auth_side == "page_left"

def test_TK_RosTel_002():
    # поиск искомых элементов
    tab_phone = pytest.engine.find_element(By.ID, "t-btn-tab-phone")
    tab_mail = pytest.engine.find_element(By.ID, "t-btn-tab-mail")
    tab_login = pytest.engine.find_element(By.ID, "t-btn-tab-login")
    tab_ls = pytest.engine.find_element(By.ID, "t-btn-tab-ls")
    # Инициализация выбора метода авторизации
    tab_mail.click()
    username_field = pytest.engine.find_element(By.CLASS_NAME, "rt-input__placeholder")
    # Проверка переключения на выбранный метод авторизации
    assert username_field.text == "Электронная почта"
    # Инициализация выбора метода авторизации
    tab_login.click()
    # Проверка переключения на выбранный метод авторизации
    assert username_field.text == "Логин"
    # Инициализация выбора метода авторизации
    tab_ls.click()
    # Проверка переключения на выбранный метод авторизации
    assert username_field.text == "Лицевой счёт"
    # Инициализация выбора метода авторизации
    tab_phone.click()
    # Проверка переключения на выбранный метод авторизации
    assert username_field.text == "Мобильный телефон"

def test_TK_RosTel_003():
    # Поиск искомых элементов
    tab_phone = pytest.engine.find_element(By.ID, "t-btn-tab-phone")
    username_field = pytest.engine.find_element(By.CLASS_NAME, "rt-input__placeholder")
    username = pytest.engine.find_element(By.ID, "username")
    # Инициализация выбора метода авторизации
    tab_phone.click()
    username.send_keys("9")
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Мобильный телефон"
    username.clear()
    username.send_keys("9")
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Мобильный телефон"
    username.clear()
    username.send_keys("3909090909")
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Мобильный телефон"
    username.clear()

def test_TK_RosTel_004():
    # Поиск искомых элементов
    tab_mail = pytest.engine.find_element(By.ID, "t-btn-tab-mail")
    username_field = pytest.engine.find_element(By.CLASS_NAME, "rt-input__placeholder")
    username = pytest.engine.find_element(By.ID, "username")
    # Инициализация выбора метода авторизации
    tab_mail.click()
    username.send_keys("goodwill@gmail.com")
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Электронная почта"
    username.clear()
    username.send_keys("goodless@mail.ru")
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Электронная почта"

def test_TK_RosTel_005():
    # Поиск искомых элементов
    tab_login = pytest.engine.find_element(By.ID, "t-btn-tab-login")
    username_field = pytest.engine.find_element(By.CLASS_NAME, "rt-input__placeholder")
    username = pytest.engine.find_element(By.ID, "username")
    # Инициализация выбора метода авторизации
    tab_login.click()
    username.send_keys("012FRGfrgАПКапк_?")
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Логин"

def test_TK_RosTel_006():
    # Поиск искомых элементов
    tab_ls = pytest.engine.find_element(By.ID, "t-btn-tab-ls")
    username_field = pytest.engine.find_element(By.CLASS_NAME, "rt-input__placeholder")
    username = pytest.engine.find_element(By.ID, "username")
    # Инициализация выбора метода авторизации
    tab_ls.click()
    username.send_keys("1")
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Лицевой счёт"
    username.clear()
    username.send_keys("123456789012")
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Лицевой счёт"

def test_TK_RosTel_007():
    # Поиск искомых элементов
    username_field = pytest.engine.find_element(By.CLASS_NAME, "rt-input__placeholder")
    username_write = pytest.engine.find_element(By.NAME, "username")
    username = pytest.engine.find_element(By.ID, "username")
    password = pytest.engine.find_element(By.ID, "password")
    tab_phone = pytest.engine.find_element(By.ID, "t-btn-tab-phone")
    # Инициализация выбора метода авторизации
    tab_phone.click()
    username.send_keys("1011011011")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Лицевой счёт"
    assert username_write.get_attribute("value") == "1011011011"
    username.clear()
    # Инициализация выбора метода авторизации
    tab_phone.click()
    username.send_keys("101101101101")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Лицевой счёт"
    assert username_write.get_attribute("value") == "101101101101"
    username.clear()
    # Инициализация выбора метода авторизации
    tab_phone.click()
    username.send_keys("012frgапк_?")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Логин"
    assert username_write.get_attribute("value") == "012frgапк_?"
    username.clear()
    # Инициализация выбора метода авторизации
    tab_phone.click()
    username.send_keys("goodless@mail.ru")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Электронная почта"
    assert username_write.get_attribute("value") == "goodless@mail.ru"
    username.clear()

def test_TK_RosTel_008():
    # Поиск искомых элементов
    username_field = pytest.engine.find_element(By.CLASS_NAME, "rt-input__placeholder")
    username_write = pytest.engine.find_element(By.NAME, "username")
    username = pytest.engine.find_element(By.ID, "username")
    password = pytest.engine.find_element(By.ID, "password")
    tab_mail = pytest.engine.find_element(By.ID, "t-btn-tab-mail")
    # Инициализация выбора метода авторизации
    tab_mail.click()
    username.send_keys("9098087076")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Мобильный телефон"
    assert username_write.get_attribute("value") == "79098087076"
    username.clear()
    # Инициализация выбора метода авторизации
    tab_mail.click()
    username.send_keys("101101101101")
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Лицевой счёт"
    assert username_write.get_attribute("value") == "101101101101"
    username.clear()
    # Инициализация выбора метода авторизации
    tab_mail.click()
    username.send_keys("012frgапк_?")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Логин"
    assert username_write.get_attribute("value") == "012frgапк_?"
    username.clear()
    # Инициализация выбора метода авторизации
    tab_mail.click()
    username.send_keys("goodless@gmail.ru")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Электронная почта"
    assert username_write.get_attribute("value") == "goodless@gmail.ru"
    username.clear()

def test_TK_RosTel_009():
    # Поиск искомых элементов
    username_field = pytest.engine.find_element(By.CLASS_NAME, "rt-input__placeholder")
    username_write = pytest.engine.find_element(By.NAME, "username")
    username = pytest.engine.find_element(By.ID, "username")
    password = pytest.engine.find_element(By.ID, "password")
    tab_login = pytest.engine.find_element(By.ID, "t-btn-tab-login")
    # Инициализация выбора метода авторизации
    tab_login.click()
    username.send_keys("9098087076")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Мобильный телефон"
    assert username_write.get_attribute("value") == "79098087076"
    username.clear()
    # Инициализация выбора метода авторизации
    tab_login.click()
    username.send_keys("101101101101")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Лицевой счёт"
    assert username_write.get_attribute("value") == "101101101101"
    username.clear()
    # Инициализация выбора метода авторизации
    tab_login.click()
    username.send_keys("012frgапк_?")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Логин"
    assert username_write.get_attribute("value") == "012frgапк_?"
    username.clear()
    # Инициализация выбора метода авторизации
    tab_login.click()
    username.send_keys("goodless@gmail.ru")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Электронная почта"
    assert username_write.get_attribute("value") == "goodless@mail.ru"
    username.clear()

def test_TK_RosTel_010():
    # Поиск искомых элементов
    username_field = pytest.engine.find_element(By.CLASS_NAME, "rt-input__placeholder")
    username_write = pytest.engine.find_element(By.NAME, "username")
    username = pytest.engine.find_element(By.ID, "username")
    password = pytest.engine.find_element(By.ID, "password")
    tab_ls = pytest.engine.find_element(By.ID, "t-btn-tab-ls")
    # Инициализация выбора метода авторизации
    tab_ls.click()
    username.send_keys("9098087076")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Мобильный телефон"
    assert username_write.get_attribute("value") == "79098087076"
    username.clear()
    # Инициализация выбора метода авторизации
    tab_ls.click()
    username.send_keys("101101101101")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Лицевой счёт"
    assert username_write.get_attribute("value") == "101101101101"
    username.clear()
    # Инициализация выбора метода авторизации
    tab_ls.click()
    username.send_keys("012frgапк_?")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Логин"
    assert username_write.get_attribute("value") == "012frgапк_?"
    username.clear()
    # Инициализация выбора метода авторизации
    tab_ls.click()
    username.send_keys("goodless@gmail.ru")
    # Инициализация клика в другое поле
    ActionChains(pytest.engine).move_to_element(password).click().perform()
    # Проверка переключения от ввода данных на нужный метод авторизации
    assert username_field.text == "Электронная почта"
    assert username_write.get_attribute("value") == "goodless@mail.ru"
    username.clear()

def test_TK_RosTel_011():
    # Поиск искомых элементов
    password = pytest.engine.find_element(By.ID, "password")
    password_eye = pytest.engine.find_element(By.CLASS_NAME, "rt-input__eye")
    # Отправка пароля
    password.send_keys("012FRGfrgАПКапк_?")
    # Инициализация показа пароля
    ActionChains(pytest.engine).move_to_element(password_eye).click().perform()
    # Проверка показа пароля
    assert password.get_attribute("type") == "text"

def test_TK_RosTel_012():
    # Поиск искомых элементов
    btn_forgot = pytest.engine.find_element(By.ID, "forgot_password")
    # Инициализация перехода к форме восстановления пароля
    ActionChains(pytest.engine).move_to_element(btn_forgot).click().perform()
    # Проверка адреса страницы перехода
    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" in str(pytest.engine.current_url)

def test_TK_RosTel_013():
    # Поиск искомых элементов
    btn_code_enter = pytest.engine.find_element(By.ID, "back_to_otp_btn")
    # Инициализация перехода к форме входа по временному коду
    ActionChains(pytest.engine).move_to_element(btn_code_enter).click().perform()
    # Проверка адреса страницы перехода
    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate" in str(pytest.engine.current_url)

def test_TK_RosTel_014():
    # Поиск искомых элементов
    btn_register = pytest.engine.find_element(By.ID, "kc-register")
    # Инициализация перехода к форме регистрации
    ActionChains(pytest.engine).move_to_element(btn_register).click().perform()
    # Проверка адреса страницы перехода
    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration" in str(pytest.engine.current_url)

def test_TK_RosTel_015():
    # Поиск искомых элементов
    btn_register = pytest.engine.find_element(By.ID, "kc-register")
    ActionChains(pytest.engine).move_to_element(btn_register).click().perform()
    WebDriverWait(pytest.engine, 90).until(EC.visibility_of_element_located((By.NAME, "register")))
    btn_registrator = pytest.engine.find_element(By.NAME, "register")
    first_name = pytest.engine.find_element(By.NAME, "firstName")
    last_name = pytest.engine.find_element(By.NAME, "lastName")
    username = pytest.engine.find_element(By.ID, "address")
    password = pytest.engine.find_element(By.ID, "password")
    password_confirm = pytest.engine.find_element(By.ID, "password-confirm")
    # Отправка данных для регистрации
    first_name.send_keys("012FRGfrgАПКапк_?")
    last_name.send_keys("012FRGfrgАПКапк_?")
    username.send_keys("012FRGfrgАПКапк_?")
    password.send_keys("012FRGfrgАПКапк_?")
    password_confirm.send_keys("012FRGfrgАПКапк_?")
    # Инициализация регистрации
    ActionChains(pytest.engine).move_to_element(btn_registrator).click().perform()
    meta_error = pytest.engine.find_elements(By.CLASS_NAME, "rt-input-container__meta")
    # Проверка показа подсказок
    assert len(meta_error) == 5

def test_TK_RosTel_016():
    # Поиск искомых элементов
    btn_register = pytest.engine.find_element(By.ID, "kc-register")
    ActionChains(pytest.engine).move_to_element(btn_register).click().perform()
    WebDriverWait(pytest.engine, 90).until(EC.visibility_of_element_located((By.NAME, "register")))
    btn_registrator = pytest.engine.find_element(By.NAME, "register")
    first_name = pytest.engine.find_element(By.NAME, "firstName")
    last_name = pytest.engine.find_element(By.NAME, "lastName")
    username = pytest.engine.find_element(By.ID, "address")
    password = pytest.engine.find_element(By.ID, "password")
    password_confirm = pytest.engine.find_element(By.ID, "password-confirm")
    # Отправка данных для регистрации
    first_name.send_keys("")
    last_name.send_keys("")
    username.send_keys("")
    password.send_keys("")
    password_confirm.send_keys("")
    # Инициализация регистрации
    ActionChains(pytest.engine).move_to_element(btn_registrator).click().perform()
    meta_error = pytest.engine.find_elements(By.CLASS_NAME, "rt-input-container__meta")
    # Проверка показа подсказок
    assert len(meta_error) == 5

def test_TK_RosTel_017():
    # Поиск искомых элементов
    btn_register = pytest.engine.find_element(By.ID, "kc-register")
    ActionChains(pytest.engine).move_to_element(btn_register).click().perform()
    WebDriverWait(pytest.engine, 90).until(EC.visibility_of_element_located((By.NAME, "register")))
    btn_registrator = pytest.engine.find_element(By.NAME, "register")
    password = pytest.engine.find_element(By.ID, "password")
    password_confirm = pytest.engine.find_element(By.ID, "password-confirm")
    # Отправка данных для проверки совместимости полей пароль - подтверждение пароля
    password.send_keys("Trevor12")
    password_confirm.send_keys("21trevoR")
    # Инициализация входа
    ActionChains(pytest.engine).move_to_element(btn_registrator).click().perform()
    meta_error = pytest.engine.find_elements(By.CLASS_NAME, "rt-input-container__meta")
    # Проверка показа подсказок
    assert len(meta_error) == 4

def test_TK_RosTel_018():
    # Внимание. Перейдите в файл settings.py и следуйте инструкции
    # Поиск искомых элементов
    btn_enter = pytest.engine.find_element(By.ID, "kc-login")
    username = pytest.engine.find_element(By.ID, "username")
    password = pytest.engine.find_element(By.ID, "password")
    tab_phone = pytest.engine.find_element(By.ID, "t-btn-tab-phone")
    # Инициализация выбора метода авторизации
    tab_phone.click()
    # Отправка данных для входа в учетную запись
    username.send_keys(valid_phone_number)
    password.send_keys("111111111")
    # Инициализация входа
    ActionChains(pytest.engine).move_to_element(btn_enter).click().perform()
    meta_error = pytest.engine.find_element(By.ID, "form-error-message")
    assert meta_error.text != ""
    # Проверка адреса страницы перехода
    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate" in str(pytest.engine.current_url)

def test_TK_RosTel_019():
    # Внимание. Перейдите в файл settings.py и следуйте инструкции
    # Поиск искомых элементов
    btn_enter = pytest.engine.find_element(By.ID, "kc-login")
    username = pytest.engine.find_element(By.ID, "username")
    password = pytest.engine.find_element(By.ID, "password")
    tab_mail = pytest.engine.find_element(By.ID, "t-btn-tab-mail")
    # Инициализация выбора метода авторизации
    tab_mail.click()
    # Отправка данных для входа в учетную запись
    username.send_keys(valid_email)
    password.send_keys("111111111")
    # Инициализация входа
    ActionChains(pytest.engine).move_to_element(btn_enter).click().perform()
    meta_error = pytest.engine.find_element(By.ID, "form-error-message")
    assert meta_error.text != ""
    # Проверка адреса страницы перехода
    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate" in str(pytest.engine.current_url)

def test_TK_RosTel_020():
    # Внимание. Перейдите в файл settings.py и следуйте инструкции
    # Поиск искомых элементов
    btn_enter = pytest.engine.find_element(By.ID, "kc-login")
    username = pytest.engine.find_element(By.ID, "username")
    password = pytest.engine.find_element(By.ID, "password")
    tab_login = pytest.engine.find_element(By.ID, "t-btn-tab-login")
    # Инициализация выбора метода авторизации
    tab_login.click()
    # Отправка данных для входа в учетную запись
    username.send_keys(valid_login)
    password.send_keys("111111111")
    # Инициализация входа
    ActionChains(pytest.engine).move_to_element(btn_enter).click().perform()
    meta_error = pytest.engine.find_element(By.ID, "form-error-message")
    assert meta_error.text != ""
    # Проверка адреса страницы перехода
    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate" in str(pytest.engine.current_url)

def test_TK_RosTel_021():
    # Внимание. Перейдите в файл settings.py и следуйте инструкции
    # Поиск искомых элементов
    btn_enter = pytest.engine.find_element(By.ID, "kc-login")
    username = pytest.engine.find_element(By.ID, "username")
    password = pytest.engine.find_element(By.ID, "password")
    tab_ls = pytest.engine.find_element(By.ID, "t-btn-tab-ls")
    # Инициализация выбора метода авторизации
    tab_ls.click()
    # Отправка данных для входа в учетную запись
    username.send_keys(valid_ls)
    password.send_keys("111111111")
    # Инициализация входа
    ActionChains(pytest.engine).move_to_element(btn_enter).click().perform()
    meta_error = pytest.engine.find_element(By.ID, "form-error-message")
    assert meta_error.text != ""
    # Проверка адреса страницы перехода
    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate" in str(pytest.engine.current_url)

def test_TK_RosTel_022():
    # Внимание. Перейдите в файл settings.py и следуйте инструкции
    # Поиск искомых элементов
    btn_enter = pytest.engine.find_element(By.ID, "kc-login")
    username = pytest.engine.find_element(By.ID, "username")
    password = pytest.engine.find_element(By.ID, "password")
    tab_phone = pytest.engine.find_element(By.ID, "t-btn-tab-phone")
    # Инициализация выбора метода авторизации
    tab_phone.click()
    # Отправка данных для входа в учетную запись
    username.send_keys(valid_phone_number)
    password.send_keys(valid_password)
    # Инициализация входа
    ActionChains(pytest.engine).move_to_element(btn_enter).click().perform()
    # Проверка адреса страницы перехода
    assert "https://start.rt.ru/?tab=main" in str(pytest.engine.current_url)

def test_TK_RosTel_023():
    # Внимание. Перейдите в файл settings.py и следуйте инструкции
    # Поиск искомых элементов
    btn_enter = pytest.engine.find_element(By.ID, "kc-login")
    username = pytest.engine.find_element(By.ID, "username")
    password = pytest.engine.find_element(By.ID, "password")
    tab_mail = pytest.engine.find_element(By.ID, "t-btn-tab-mail")
    # Инициализация выбора метода авторизации
    tab_mail.click()
    # Отправка данных для входа в учетную запись
    username.send_keys(valid_email)
    password.send_keys(valid_password)
    # Инициализация входа
    ActionChains(pytest.engine).move_to_element(btn_enter).click().perform()
    # Проверка адреса страницы перехода
    assert "https://start.rt.ru/?tab=main" in str(pytest.engine.current_url)

def test_TK_RosTel_024():
    # Внимание. Перейдите в файл settings.py и следуйте инструкции
    # Поиск искомых элементов
    btn_enter = pytest.engine.find_element(By.ID, "kc-login")
    username = pytest.engine.find_element(By.ID, "username")
    password = pytest.engine.find_element(By.ID, "password")
    tab_login = pytest.engine.find_element(By.ID, "t-btn-tab-login")
    # Инициализация выбора метода авторизации
    tab_login.click()
    # Отправка данных для входа в учетную запись
    username.send_keys(valid_login)
    password.send_keys(valid_password)
    # Инициализация входа
    ActionChains(pytest.engine).move_to_element(btn_enter).click().perform()
    # Проверка адреса страницы перехода
    assert "https://start.rt.ru/?tab=main" in str(pytest.engine.current_url)

def test_TK_RosTel_025():
    # Внимание. Перейдите в файл settings.py и следуйте инструкции
    # Поиск искомых элементов
    btn_enter = pytest.engine.find_element(By.ID, "kc-login")
    username = pytest.engine.find_element(By.ID, "username")
    password = pytest.engine.find_element(By.ID, "password")
    tab_ls = pytest.engine.find_element(By.ID, "t-btn-tab-ls")
    # Инициализация выбора метода авторизации
    tab_ls.click()
    # Отправка данных для входа в учетную запись
    username.send_keys(valid_ls)
    password.send_keys(valid_password)
    # Инициализация входа
    ActionChains(pytest.engine).move_to_element(btn_enter).click().perform()
    # Проверка адреса страницы перехода
    assert "https://start.rt.ru/?tab=main" in str(pytest.engine.current_url)
