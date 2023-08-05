from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, '[value="Добавить в корзину"]')
    PRICE_CART = (By.XPATH, "//p[contains(text(), 'Стоимость корзины теперь составляет')]/strong")
    PRICE_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main > .price_color")
    NAME_BOOK_CART = (By.XPATH, "//div[@id='messages']/div[1]/div[1]/strong")
    NAME_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")