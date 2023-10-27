import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_availability_of_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(2)
    basket = browser.find_element(By.ID, "add_to_basket_form")
    assert basket.is_displayed(), "Кнопка добавления в корзину не найдена или скрыта"

