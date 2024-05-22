from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.ui import Select


class Test_CartPricePage:

    def test_check_load_image(self, browser):
        browser.get(f"http://192.168.1.147:8081/en-gb/product/apple-cinema")
        assert not browser.find_element(By.XPATH, "//*[@id='content']//*/img").get_property("src") is None

    def test_check_name_product(self, browser):
        browser.get(f"http://192.168.1.147:8081/en-gb/product/apple-cinema")
        assert browser.find_elements(By.CSS_SELECTOR, ".col-sm")[1].find_element(By.CSS_SELECTOR,
                                                                                 "h1").text == 'Apple Cinema 30"'

    def test_check_radio_button(self, browser):
        browser.get(f"http://192.168.1.147:8081/en-gb/product/apple-cinema")
        elements_radio_button = browser.find_element(By.CSS_SELECTOR, "#input-option-218").find_elements(
            By.CSS_SELECTOR, ".form-check")
        for button in elements_radio_button:
            AC(browser).move_to_element(button.find_element(By.CSS_SELECTOR, ".form-check-input")).click().perform()

    def test_check_checkbox(self, browser):
        browser.get(f"http://192.168.1.147:8081/en-gb/product/apple-cinema")
        elements_checkbox = browser.find_element(By.CSS_SELECTOR, "#input-option-223").find_elements(By.CSS_SELECTOR,
                                                                                                     ".form-check")
        for button in elements_checkbox:
            AC(browser).move_to_element(button.find_element(By.CSS_SELECTOR, ".form-check-input")).click().perform()

    def test_select_list(self, browser):
        browser.get(f"http://192.168.1.147:8081/en-gb/product/apple-cinema")
        Select(browser.find_element(By.CSS_SELECTOR, "#input-option-217")).select_by_index(4)
