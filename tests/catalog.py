from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class Test_CatalogPage:

    def test_catalog(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb/catalog/desktops")
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#product-list")))

    def test_check_collection_catalog(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb/catalog/desktops")
        assert browser.find_element(By.CSS_SELECTOR,
                                    ".row.row-cols-1.row-cols-sm-2.row-cols-md-2.row-cols-lg-3").find_elements(
            By.CSS_SELECTOR, ".col.mb-3") != []

    def test_check_function_compare(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb/catalog/desktops")
        browser.find_element(By.CSS_SELECTOR, "#compare-total").is_displayed()

    def test_check_filters(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb/catalog/desktops")
        browser.find_element(By.CSS_SELECTOR, "#button-list").is_enabled()
        browser.find_element(By.CSS_SELECTOR, "#button-grid").is_enabled()

    def test_open_cart_priec(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb/catalog/desktops")
        AC(browser).click(browser.find_element(By.LINK_TEXT, 'Apple Cinema 30"')).perform()
