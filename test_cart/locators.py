import pytest
from selenium.webdriver.common.by import By
from conftest import browser


def test_locators(browser):
    browser.get("https://www.saucedemo.com/")
    username = browser.find_element(By.ID, "user-name")
    # By.NAME
    password = browser.find_element(By.NAME, "password")
    # By.CLASS_NAME
    login_button = browser.find_element(By.CLASS_NAME, "submit-button")
    # By.TAG_NAME
    browser.find_element(By.TAG_NAME, "form")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    browser.get("https://www.saucedemo.com/inventory.html")
    # By.LINK_TEXT
    browser.find_element(By.LINK_TEXT, "Sauce Labs Fleece Jacket")
    # By.PARTIAL_LINK_TEXT
    browser.find_element(By.PARTIAL_LINK_TEXT, "Bolt T-Shirt")
    browser.get("https://www.saucedemo.com/cart.html")
    # Поиск по атрибуту: // tag[ @ attribute = 'value']
    browser.find_element(By.XPATH, "//button[@data-test='checkout']")
    browser.get("https://www.saucedemo.com/inventory.html")
    # Поиск по тексту: //tag[text()='text']
    browser.find_element(By.XPATH, "//button[text()='Add to cart']")
    # Частичное совпадение атрибута: //tag[contains(@attribute,'text')]
    browser.find_element(By.XPATH, "//img[contains(@alt, 'Sauce Labs Bike Light')]")
    # Частичное совпадение текста: //tag[contains(text(),'text')]
    browser.find_element(By.XPATH, "//button[contains(text(), 'Add to cart')]")

    # Поиск по осям XPath

    # ancestor
    browser.find_element(By.XPATH, "//select[contains(@class, 'product_sort_container')]/ancestor::div[1]")
    # descendant
    browser.find_element(By.XPATH, "//select[contains(@class, 'product_sort_container')]/ancestor::div[1]")
    # following
    browser.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/following::*[1]")
    # parent
    browser.find_element(By.XPATH, "//select[@class='product_sort_container']/parent::*[1]")
    # preceding
    browser.find_element(By.XPATH, "//select[contains(@class, 'product_sort_container')]/preceding::*[1]")
    # Поиск с условием and: //input[@name='user-name' and @type='text']
    browser.find_element(By.XPATH, "//div[@class='app_logo' and text()='Swag Labs']")

    # CSS - селекторы

    # .class
    browser.find_element(By.CSS_SELECTOR, ".product_sort_container")
    # .class1.class2
    browser.find_element(By.CSS_SELECTOR, ".btn.btn_primary")
    # .class1 .class2
    browser.find_element(By.CSS_SELECTOR, ".product_sort_container option")
    # #id
    browser.find_element(By.CSS_SELECTOR, "#add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)")
    # tagname
    browser.find_element(By.CSS_SELECTOR, "select")
    # tagname.class
    browser.find_element(By.CSS_SELECTOR, "select.product_sort_container")
    # [attribute=value]
    browser.find_element(By.CSS_SELECTOR, "[data-test='product-sort-container']")
    # [attribute~=value]
    browser.find_element(By.CSS_SELECTOR, "[class~='product_sort_container']")
    # [attribute|=value]
    browser.find_element(By.CSS_SELECTOR, "[data-test|='add-to-cart']")
    # [attribute^=value]
    browser.find_element(By.CSS_SELECTOR, "[class^='product']")
    # [attribute$=value]
    browser.find_element(By.CSS_SELECTOR, "[class$='container']")
    # [attribute*=value]
    browser.find_element(By.CSS_SELECTOR, "[class*='sort']")


