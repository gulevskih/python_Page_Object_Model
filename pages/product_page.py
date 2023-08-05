from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):

    def add_item_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()

    def should_be_login_url(self):
        assert "?promo=newYear" in self.browser.current_url, "Login url is not correct"

    def should_be_price(self):
        price_cart = self.browser.find_element(*ProductPageLocators.PRICE_CART).text
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        assert price_cart == price_book, "Price of the cart does not match the price of the book"

    def should_be_name_book(self):
        name_book_cart = self.browser.find_element(*ProductPageLocators.NAME_BOOK_CART).text
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        assert name_book_cart == name_book, "Name's book of the cart does not match name's book"