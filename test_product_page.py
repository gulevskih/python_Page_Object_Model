from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_login_url()
    page.should_be_price()
    page.should_be_name_book()