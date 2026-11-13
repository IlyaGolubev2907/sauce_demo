import pytest
from selenium.webdriver.common.by import By
from conftest import browser


def test_cart(browser):
    browser.get("https://www.saucedemo.com/")
    username = browser.find_element(By.ID, "user-name")
    password = browser.find_element(By.NAME, "password")
    login_button = browser.find_element(By.CLASS_NAME, "submit-button")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    browser.get("https://www.saucedemo.com/inventory.html")
    expected_item_name = browser.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    expected_item_price = browser.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    add_to_cart_button.click()
    shopping_cart_button = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    shopping_cart_button.click()
    actual_item_name = browser.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    actual_item_price = browser.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
    assert actual_item_name == expected_item_name, "Название товара не совпадает"
    assert actual_item_price == expected_item_price, "Цена товара не совпадает"
