import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.ui import Select


class Test_MainPage:

    def test_CheckMainPage(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=common/home")
        WebDriverWait(browser, 1).until(EC.title_is("Your Store"))
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#logo")))
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search")))
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header-cart")))
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))

    def test_CheckNagivationBar(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=common/home")
        list_item_bar = ["Desktops", "Laptops & Notebooks", "Components", "Tablets", "Software", "Phones & PDAs",
                         "Cameras",
                         "MP3 Players"]
        navigation = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#menu")))
        for item in list_item_bar:
            navigation.find_element(By.LINK_TEXT, f"{item}")

    def test_OpenCatalog(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=common/home")
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#narbar-menu")))
        AC(browser).move_to_element(browser.find_element(By.LINK_TEXT, "Desktops")).perform()
        AC(browser).move_to_element(browser.find_element(By.LINK_TEXT, "Show All Desktops")).click().perform()


class Test_CatalogPage:

    def test_Catalog(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb/catalog/desktops")
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#product-list")))

    def test_CheckCollectionCatalog(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb/catalog/desktops")
        assert browser.find_element(By.CSS_SELECTOR,
                                    ".row.row-cols-1.row-cols-sm-2.row-cols-md-2.row-cols-lg-3").find_elements(
            By.CSS_SELECTOR, ".col.mb-3") != []

    def test_CheckFunctionCompare(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb/catalog/desktops")
        browser.find_element(By.CSS_SELECTOR, "#compare-total").is_displayed()

    def test_CheckFilters(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb/catalog/desktops")
        browser.find_element(By.CSS_SELECTOR, "#button-list").is_enabled()
        browser.find_element(By.CSS_SELECTOR, "#button-grid").is_enabled()

    def test_OpenCartPrice(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb/catalog/desktops")
        AC(browser).click(browser.find_element(By.LINK_TEXT, 'Apple Cinema 30"')).perform()


class Test_CartPricePage:

    def test_CheckLoadImage(self, browser):
        browser.get(f"http://192.168.1.147:8081/en-gb/product/apple-cinema")
        assert not browser.find_element(By.XPATH, "//*[@id='content']//*/img").get_property("src") is None

    def test_CheckNameProduct(self, browser):
        browser.get(f"http://192.168.1.147:8081/en-gb/product/apple-cinema")
        assert browser.find_elements(By.CSS_SELECTOR, ".col-sm")[1].find_element(By.CSS_SELECTOR,
                                                                                 "h1").text == 'Apple Cinema 30"'

    def test_CheckRadioButton(self, browser):
        browser.get(f"http://192.168.1.147:8081/en-gb/product/apple-cinema")
        elements_radio_button = browser.find_element(By.CSS_SELECTOR, "#input-option-218").find_elements(
            By.CSS_SELECTOR, ".form-check")
        for button in elements_radio_button:
            AC(browser).move_to_element(button.find_element(By.CSS_SELECTOR, ".form-check-input")).click().perform()

    def test_CheckCheckBox(self, browser):
        browser.get(f"http://192.168.1.147:8081/en-gb/product/apple-cinema")
        elements_checkbox = browser.find_element(By.CSS_SELECTOR, "#input-option-223").find_elements(By.CSS_SELECTOR,
                                                                                                     ".form-check")
        for button in elements_checkbox:
            AC(browser).move_to_element(button.find_element(By.CSS_SELECTOR, ".form-check-input")).click().perform()

    def test_SelectList(self, browser):
        browser.get(f"http://192.168.1.147:8081/en-gb/product/apple-cinema")
        Select(browser.find_element(By.CSS_SELECTOR, "#input-option-217")).select_by_index(4)


class TestAdmin:
    def test_CheckExistsElement(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        browser.find_element(By.CSS_SELECTOR, "#header")
        browser.find_element(By.CSS_SELECTOR, "#content")
        browser.find_element(By.CSS_SELECTOR, "#footer")

    def test_SetUserName(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("admin")

    def test_SetPassword(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("1234")

    def test_CheckEnabledButton(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").is_enabled()

    def test_CheckTitle(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        assert browser.title == "Administration"


class TestRegistration:
    def test_CheckExistsElement(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=account/register")
        browser.find_element(By.CSS_SELECTOR, "#top")
        browser.find_element(By.CSS_SELECTOR, "#header-cart")
        browser.find_element(By.CSS_SELECTOR, "#account-register")
        browser.find_elements(By.CSS_SELECTOR, ".container")

    def test_CheckEnabledCheckBox(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=account/register")
        checkbox = browser.find_elements(By.CSS_SELECTOR, ".form-check-input")
        for element in checkbox:
            element.is_enabled()

    def test_CheckNeedWrite(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=account/register")
        check_items = ["input-firstname", "input-lastname", "input-email", "input-password"]
        for element in check_items:
            browser.find_element(By.CSS_SELECTOR, f"#{element}").send_keys("test")
            browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()


class TestPart3:

    def test_LoginForAdmin(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("user")
        browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("12345678")
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
        WebDriverWait(browser, 1).until(EC.title_is("Dashboard"))

    def test_SelectRandomProduct(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=common/home")
        elements_product = browser.find_element(By.CSS_SELECTOR, "#content").find_element(By.CSS_SELECTOR,
                                                                                          ".row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4").find_elements(
            By.CSS_SELECTOR, ".col.mb-3")
        random_element = random.choice(elements_product)
        random_element.find_element(By.CSS_SELECTOR, ".fa-solid.fa-shopping-cart").click()
        WebDriverWait(browser, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")))

    def test_ValueForMain(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=common/home")
        value_first_element = browser.find_element(By.CSS_SELECTOR, '.price-new').text
        AC(browser).move_to_element(browser.find_element(By.CSS_SELECTOR, ".dropdown")).click().perform()
        AC(browser).move_to_element(browser.find_element(By.LINK_TEXT, "€ Euro")).click().perform()
        new_value_first_element = browser.find_element(By.CSS_SELECTOR, '.price-new').text
        assert value_first_element != new_value_first_element

    def test_ValueForCatalog(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb/catalog/desktops")
        value_first_element = browser.find_element(By.CSS_SELECTOR, '.price-new').text
        AC(browser).move_to_element(browser.find_element(By.CSS_SELECTOR, ".dropdown")).click().perform()
        AC(browser).move_to_element(browser.find_element(By.LINK_TEXT, "€ Euro")).click().perform()
        new_value_first_element = browser.find_element(By.CSS_SELECTOR, '.price-new').text
        assert value_first_element != new_value_first_element
